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
from flask import jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import boto3
import pandas as pd
import PIL.Image as Image
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from config import configure_MongoDB, mongodb_connect, aws_s3




# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

bucket_name = 'returnedimages'
# directory_prefix = ''

class_names = ["T-Shirt/Top", "Trouser", "Pullover", "Dress",
               "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]



def load_model_trained():
    """
    This function load the traned model.
    Return:
    """
    global model
    model = tf.keras.models.load_model("train_model.h5", compile=False)
    print("Model loaded")



# session, s3_client = aws_s3()

# images_directory = s3_client.list_objects(Bucket=bucket_name)


# classified_images = []


@app.route('/')
def index():
     """
     This function is a simple index page.
     Return: Text on the 'Simple API to classify returns images, with Flask! '
     """
     return 'Simple API to classify returns images, with Flask! '


@app.route("/classify", methods=['POST', 'GET'])
def classify():
    """
    This function is the API Endpoint. It takes images from the images directory, preprocesses them, and classifies them in batch.
    The function only classifies new images in the directory.
    Return: Classification of new images; otherwise, return 'No new images to classify'
    """
    now = datetime.datetime.now()
    data_list = []
    classified_images = set()
    found_new_images = False
    images_path = "/Users/buhariabubakar/Desktop/Image_classification/images"
      # Load the existing classified image filenames from the CSV file
   
    if os.path.isfile('classification.csv'):
        existing_data = pd.read_csv('classification.csv')
        classified_images = set(existing_data['image_name'])

    

    # Iterate over the files in the image directory
    for image_filename in os.listdir(images_path):
        if image_filename in classified_images:
            continue

        image_path = os.path.join(images_path, image_filename)

        try:
            image = Image.open(image_path)
            pre_processed_im = processing_img(image)  
            results = model.predict(pre_processed_im)
            single_results = results[0]
            class_label = int(np.argmax(single_results))
            class_likelihood = single_results[class_label]
            class_name = class_names[class_label]
            found_new_images = True
            
            data_list.append({
                'image_name': image_filename,
                'label': class_name,
                'probability': float(class_likelihood),
                'date': now.strftime("%d %b %Y"),
                'time': now.strftime("%H:%M:%S")
            })
            classified_images.add(image_filename)
        except Exception as e:
            print(f"Error processing image {image_filename}: {e}")

    if not found_new_images:
        message = {
            'message': 'No new images to classify'
        }
        return jsonify(message)
    
    # Storing the classified result in MongoDB
    # collection = mongodb_connect()
    # result_json = json.loads(dumps(data_list, default=str))
    # collection.insert_many(result_json)

  
        # Storing the classified result in CSV
    dataframe = pd.DataFrame(data_list)
    # csv_file_path = os.path.join(os.getcwd(), 'classification.csv')
    # print("Current working directory before saving:", os.getcwd())
    # dataframe.to_csv(csv_file_path, mode='a', header=not os.path.isfile(csv_file_path), index=False)
    # workspace_directory = "/Users/buhariabubakar/.jenkins/war/workspace/batch_images_classification"
    # print("Jenkins workspace directory:", workspace_directory)
    # Storing the classified result in the Jenkins workspace directory
    workspace_dir = "/Users/buhariabubakar/.jenkins/workspace/batch_images_classification"
    csv_file_path = os.path.join(workspace_dir, 'classification.csv')
    dataframe.to_csv(csv_file_path, mode='a', header=not os.path.isfile(csv_file_path), index=False)

    # # Commit and push the classification results to GitHub
    # os.system('cd' + workspace_dir)
    # os.system('git fetch origin')
    # os.system('git add classification.csv')
    # os.system('git commit -m "Add classification results"')
    # os.system('git push origin HEAD:master')
    # Change directory to the workspace
    os.chdir(workspace_dir)

    # Pull the latest changes from the remote repository
    os.system('git pull')

    # Commit and push the classification results to GitHub
    os.system('git add classification.csv')
    os.system('git commit -m "Add classification results"')
    os.system('git push origin HEAD:master')

    return jsonify(data_list)



if __name__ == "__main__":
    print("Loading the model please wait")

    load_model_trained()
    app.run(debug=True)
    
    






