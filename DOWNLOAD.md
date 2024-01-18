Dataset **Danish Golf Courses Orthophotos** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://www.dropbox.com/scl/fi/exk4wabqtflii4zxhcqu2/danish-golf-courses-orthophotos-DatasetNinja.tar?rlkey=phz8dl4o1ix3xbiit7yt9hmuy&dl=1)

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