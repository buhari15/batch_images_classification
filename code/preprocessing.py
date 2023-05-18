from tensorflow import keras

from PIL import Image
import io
import os
import numpy as np


def processing_img(img):
    img = img.convert('L')  # Convert image to grayscale
    img = img.resize((28, 28))  # Resize image to (28, 28)
    img_array = np.array(img)  # Convert PIL image to NumPy array
    img_array = img_array / 255.0  # Normalize pixel values to the range [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension at the beginning
    return img_array


# def processing_img(img):
#     img = keras.utils.load_img(img, color_mode="grayscale", target_size=(28, 28))
#     img = keras.utils.img_to_array(img)
#     img = np.expand_dims(img, 0)
#     images = np.vstack([img])

#     return images


