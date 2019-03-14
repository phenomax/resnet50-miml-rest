# A [CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network) model for the [MIML](http://lamda.nju.edu.cn/data_MIMLimage.ashx) dataset built with [FastAI](https://github.com/fastai/fastai/), ResNet-50 and [Flask](http://flask.pocoo.org/)
In this repository you'll find:

-  My [Jupyter Notebook](https://jupyter.org/) file for the training of a ResNet-50 based [CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network) using [FastAI](https://github.com/fastai/fastai/)
- A ready to use [REST-API](https://en.wikipedia.org/wiki/Representational_state_transfer) in [Flask](http://flask.pocoo.org/), which returns predictions for any given image

## Using the Jupyter-Notebook file

You need to have `fastai>=1.0.0` installed.

## Setup the REST-API

Please note, that i put my `weights.pkl` file in the `rest-api` folder. If you modified the model, you have to export your weights and replace the file.

Install requirements

```bash
pip install -r rest-api/requirements.txt
```

Start server

```bash
FLASK_APP=rest-api/server.py flask run
```

Make a demo request

```bash
python request.py --file example.jpg
# Returns: {'result': 'desert'}
```

