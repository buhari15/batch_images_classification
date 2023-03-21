from tensorflow import keras

from PIL import Image
import io
import os
import numpy as np


def processing_img(img):
    img = keras.utils.load_img(img, color_mode="grayscale", target_size=(28, 28))
    img = keras.utils.img_to_array(img)
    img = np.expand_dims(img, 0)
    images = np.vstack([img])

    return images


