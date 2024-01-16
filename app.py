import os
from flask_cors import CORS, cross_origin
from dogCatClassifier.utils import decodeImage
from dogCatClassifier.pipeline.predict import DogCat
from flask import Flask, request, jsonify, render_template

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.file_name = "inputImage.jpg"
        self.classifier = DogCat(self.file_name)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods = ['POST'])
@cross_origin()
def predict():
    image = request.json['image']
    decodeImage(image, clApp.file_name)
    result = clApp.classifier.predict_dog_cat()
    return jsonify(result)

@app.route("/train", methods = ['GET'])
@cross_origin()
def train():
    os.system("python main.py")
    return "Training done successfully!"

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8080)