from tensorflow import keras

from PIL import Image
import io
import os
import numpy as np


def processing_img(img):
    """
    This function preprocess the images before classification.
    Return: array of images
    """
    img = img.convert('L')  
    img = img.resize((28, 28))  
    img_array = np.array(img)  
    img_array = img_array / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  
    return img_array





