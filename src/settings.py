from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Danish Golf Courses Orthophotos"
PROJECT_NAME_FULL: str = "Danish Golf Courses Orthophotos"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.ODbL_1_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Sports()]
CATEGORY: Category = Category.Sports(extra=[Category.Aerial(), Category.Satellite()])

CV_TASKS: List[CVTask] = [CVTask.InstanceSegmentation(), CVTask.SemanticSegmentation(), CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2023

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/jacotaco/danish-golf-courses-orthophotos"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 6768777
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/danish-golf-courses-orthophotos"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = "https://www.kaggle.com/datasets/jacotaco/danish-golf-courses-orthophotos/download?datasetVersionNumber=1"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "fairway": [77,156,77],
    "green": [142,243,122],
    "tee": [250,36,0],
    "bunker": [246,246,158],
    "water": [46,200,231],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://vbn.aau.dk/ws/portalfiles/portal/526716754/AI_Sports_CAMERA_READY_Semantic_Segmentation_of_Golf_Courses_for_Course_Rating_Assistance.pdf"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = None

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = ["Jesper Kjærgaard Mortensen", "Vinicius Soares Matthiesen", "Jacobo Gonzalez de Frutos", "Kata Bujdoso", "Jesper Thøger Christensen", "Andreas Møgelmose"]
AUTHORS_CONTACTS: Optional[List[str]] = ["jkjar18@student.aau.dk", "vmatth19@student.aau.dk", "jgonza22@student.aau.dk", "kbujdo22@student.aau.dk", "kbujdo22@student.aau.dk", "anmo@create.aau.dk"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Aalborg Univeristy, Denmark"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.en.aau.dk/"

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {"__PRETEXT__": "Additionally, images are tagged by 106 ***golf course*** groups. Explore them in the supervisely labeling tool"}
TAGS: Optional[List[str]] = ['multi-view']


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
