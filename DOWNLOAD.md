Dataset **Danish Golf Courses Orthophotos** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/D/5/Hg/dPnQPniTpznxJhlsgFQACVILItnJy6qBsfdOHCpbdgLuuvKxCmlKlCoM7zPIF7hv0JNuLAH72M2SsCDWzE3NEQ78nsHb8Y9XOfEboO89ZH1ynwVxmwRZ3fDIoEEW.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Danish Golf Courses Orthophotos', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/jacotaco/danish-golf-courses-orthophotos/download?datasetVersionNumber=1).