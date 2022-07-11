import numpy as np
from PIL import Image

# open theta matrix file Theta11
Theta11 = np.loadtxt('../Theta11')
Theta22 = np.loadtxt('../Theta22')


def predict_image(image_path):
    img = np.array(Image.open(image_path))
    img = img.reshape(1600, 1)

    return predict(img)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def predict(image_pixels):
    input_layer = image_pixels.copy()
    input_layer = np.append(1, input_layer)

    hidden_layer = sigmoid(np.dot(Theta11, input_layer))
    hidden_layer = np.append(1, hidden_layer)

    output_layer = sigmoid(np.dot(Theta22, hidden_layer))

    # find index of max value in output_layer
    ind = np.argmax(output_layer)
    labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return labels[ind]