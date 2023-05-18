import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from keras.datasets import fashion_mnist
import tensorflow as tf
from sklearn.metrics import classification_report


def evaluate_model():
    """
    This function evalauate the model meterics.
    Return: accuracy, precision, recall, f1 
    """

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

    load_model_trained()

    y_pred = model.predict(x_test)

    # Convert predictions to class labels
    y_pred_labels = np.argmax(y_pred, axis=1)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred_labels)
    precision = precision_score(y_test, y_pred_labels, average='weighted')
    recall = recall_score(y_test, y_pred_labels, average='weighted')
    f1 = f1_score(y_test, y_pred_labels, average='weighted')

    return accuracy, precision, recall, f1

accuracy, precision, recall, f1 = evaluate_model()

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
