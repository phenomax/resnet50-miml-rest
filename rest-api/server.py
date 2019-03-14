import io
import os
from flask import Flask, request, jsonify
from PIL import Image
from resnet_model import MyResnetModel

app = Flask(__name__)

# max filesize 2mb
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


# setup resnet model
model = MyResnetModel(os.path.dirname(os.path.abspath(__file__)))

@app.route("/")
def hello():
    return jsonify({"message": "Hello from the API"})


@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "Missing file in request"})

    img = request.files['image']

    return jsonify({"result": model.predict(img.read())})
