# https://www.kaggle.com/datasets/jacotaco/danish-golf-courses-orthophotos

import os
import shutil
from urllib.parse import unquote, urlparse

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from dotenv import load_dotenv
from supervisely._utils import camel_to_snake
from supervisely.io.fs import (
    file_exists,
    get_file_ext,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s
from dataset_tools.convert import unpack_if_archive


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

        fsize = api.file.get_directory_size(team_id, teamfiles_dir)
        with tqdm(
            desc=f"Downloading '{file_name_with_ext}' to buffer...",
            total=fsize,
            unit="B",
            unit_scale=True,
        ) as pbar:        
            api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)
        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                fsize = api.file.get_directory_size(team_id, teamfiles_dir)
                with tqdm(
                    desc=f"Downloading '{file_name_with_ext}' to buffer...",
                    total=fsize,
                    unit="B",
                    unit_scale=True,
                ) as pbar:
                    api.file.download(team_id, teamfiles_path, local_path, progress_cb=pbar)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpack_if_archive(local_path)
            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path
    
def count_files(path, extension):
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count
    
def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:

    # project_name = "Danish Golf Courses Orthophotos"
    images_path = "/home/grokhi/rawdata/danish-golf-courses-orthophotos/1. orthophotos"
    masks_path = "/home/grokhi/rawdata/danish-golf-courses-orthophotos/3. class masks"
    ds_name = "ds"
    batch_size = 30
    masks_ext = ".png"

    def create_ann(image_path):
        labels = []
        img_height = 900
        img_wight = 1600

        image_name = get_file_name(image_path)

        court_name = image_name.split("_1000")[0].lower().replace("_"," ")
        # tags = [sly.Tag(tag_meta) for tag_meta in tag_metas if tag_meta.name == court_name]        
        
        group_id = sly.Tag(tag_id, value=court_name)
        mask_path = os.path.join(masks_path, image_name + masks_ext)
        mask_np = sly.imaging.image.read(mask_path)[:, :, 0]

        for pixel in np.unique(mask_np)[1:]:
            obj_class = pixel_to_obj_class[pixel]
            mask = mask_np == pixel
            ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
            for i in range(1, ret):
                obj_mask = curr_mask == i
                curr_bitmap = sly.Bitmap(obj_mask)
                if curr_bitmap.area > 50:
                    curr_label = sly.Label(curr_bitmap, obj_class)
                    labels.append(curr_label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[group_id])


    obj_class_fairway = sly.ObjClass("fairway", sly.Bitmap)
    obj_class_green = sly.ObjClass("green", sly.Bitmap)
    obj_class_tee = sly.ObjClass("tee", sly.Bitmap)
    obj_class_bunker = sly.ObjClass("bunker", sly.Bitmap)
    obj_class_water = sly.ObjClass("water", sly.Bitmap)

    pixel_to_obj_class = {
        1: obj_class_fairway,
        2: obj_class_green,
        3: obj_class_tee,
        4: obj_class_bunker,
        5: obj_class_water,
    }

    tag_id = sly.TagMeta("golf course", sly.TagValueType.ANY_STRING)
    group_tag_name = "golf course"
    group_tag_meta = sly.TagMeta(group_tag_name, sly.TagValueType.ANY_STRING)


    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[
            obj_class_fairway,
            obj_class_green,
            obj_class_tee,
            obj_class_bunker,
            obj_class_water,
        ],
        tag_metas=[group_tag_meta]
    )
    api.project.update_meta(project.id, meta.to_json())
    api.project.images_grouping(id=project.id, enable=True, tag_name=group_tag_name)

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_names = os.listdir(images_path)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes_batch = [os.path.join(images_path, image_name) for image_name in img_names_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, images_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns_batch = [create_ann(image_path) for image_path in images_pathes_batch]
        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(img_names_batch))
    return project


