Dataset **Danish Golf Courses Orthophotos** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMjQ4Ml9EYW5pc2ggR29sZiBDb3Vyc2VzIE9ydGhvcGhvdG9zL2RhbmlzaC1nb2xmLWNvdXJzZXMtb3J0aG9waG90b3MtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiTjEwSit0V0hSblhySE1DeTMwZ2Erb0xPbzZYK1o5MG1HSkNMZDlMa2d4QT0ifQ==?response-content-disposition=attachment%3B%20filename%3D%22danish-golf-courses-orthophotos-DatasetNinja.tar%22)

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