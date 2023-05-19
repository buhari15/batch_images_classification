import keras
import numpy as np
from keras.utils import np_utils
from keras import utils as np_utils
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
import matplotlib.pyplot as plt
from tensorflow import keras


print("Data loaded")
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
assert x_train.shape == (60000, 28, 28)
assert x_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)

# Normalization
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train = x_train / 255
x_test = x_test / 255

x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

class_names = ["T-Shirt/Top", "Trouser", "Pullover", "Dress",
               "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

input_shape = (28, 28, 1)


def train_model():
    """
    this function train the model with
    keras sequential API with two convolutional blocks
    :return: the trained model
    """

    model = keras.models.Sequential(
        [
            # First convolutional block
            keras.layers.Conv2D(32, (3, 3), padding="same", activation="relu", input_shape=input_shape),
            keras.layers.Conv2D(32, (3, 3), activation="relu"),

            keras.layers.MaxPooling2D(pool_size=(2, 2)),
            keras.layers.Dropout(0.25),

            # Second convolutional block
            keras.layers.Conv2D(64, (3, 3), padding="same", activation="relu"),
            keras.layers.Conv2D(64, (3, 3), activation="relu"),

            keras.layers.MaxPooling2D(pool_size=(2, 2)),
            keras.layers.Dropout(0.25),

            keras.layers.Flatten(),

            keras.layers.Dense(500, activation="relu"),
            keras.layers.Dense(100, activation="relu"),
            keras.layers.Dropout(0.5),
            keras.layers.Dense(10, activation="softmax"),
        ]
    )

    # compiling the model
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )
    model.summary()

    return model


def model_fit(model):
    """"
    This function fit the above train_model function
    """
    history = model.fit(x_train, y_train, batch_size=32, epochs=1, validation_data=(x_test, y_test),
                            shuffle=True)
    return history

#
# model = train_model()
#
# fit_model = model_fit(model)
