import tensorflow as tf
from tensorflow import keras
from PIL import Image
import io
import flask
from werkzeug.serving import run_simple
import os
import numpy as np
from preprocessing import processing_img
from datetime import datetime
import datetime
import json


app = flask.Flask(__name__)

model = None
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

class_names = ["T-Shirt/Top", "Trouser", "Pullover", "Dress",
               "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]


def load_model_trained():
    global model
    model = tf.keras.models.load_model("train_model.h5", compile=False)
    print("Model loaded")


images_path = "/Users/buhariabubakar/Desktop/from_model_to_production/images"


@app.route("/classify", methods=['POST', 'GET'])
def classify():
    now = datetime.datetime.now()
    images_lists = images_path
    data_list = []
    for ix in os.listdir(images_lists):
        pre_processed_im = processing_img(images_lists + '//' + ix)
        results = model.predict(pre_processed_im)
        single_results = results[0]
        class_label = int(np.argmax(single_results))
        class_likelihood = single_results[class_label]
        class_name = class_names[class_label]
        
        data = {
            'images_name': ix,
            'label': class_name,
            'probability': class_likelihood,
            'date': now.strftime("%d %b %G" ),
            'time': now.strftime("%H:%M")
        
        }
    data_list.append(data)

    return flask.jsonify(str(data_list))


if __name__ == "__main__":
    print("Loading the model please wait")

    load_model_trained()
    app.run(debug=True, port=9191, threaded=True)
    






