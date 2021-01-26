import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from pathlib import Path
import sklearn.datasets
import sklearn.linear_model
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from scipy.special import softmax

data_folder = Path("data")
train_data = data_folder / "train_data.csv"
test_data = data_folder / "test_data.csv"

df = pd.read_csv(train_data)
df.head()

np.random.seed(0)


def forward_prop(model, a0):
    '''
    This is the forward propagation function
    '''
    # Load parameters from model
    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'], model['W3'], model['b3']
    # Do the first Linear step
    z1 = a0.dot(W1) + b1
    # Put it through the first activation function
    a1 = np.tanh(z1)
    # Second linear step
    z2 = a1.dot(W2) + b2
    # Put through second activation function
    a2 = np.tanh(z2)
    # Third linear step
    z3 = a2.dot(W3) + b3
    # For the Third linear activation function we use the softmax function
    a3 = softmax(z3)
    # Store all results in these values
    cache = {'a0': a0, 'z1': z1, 'a1': a1,
             'z2': z2, 'a2': a2, 'a3': a3, 'z3': z3}
    return cache


def backward_prop(model, cache, y):
    # Load parameters from model
    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'], model['W3'], model['b3']
    # Load forward propagation results
    a0, a1, a2, a3 = cache['a0'], cache['a1'], cache['a2'], cache['a3']
    # Get number of samples
    m = y.shape[0]
    # Calculate loss derivative with respect to output
    dz3 = loss_derivative(y=y, y_hat=a3)
    # Calculate loss derivative with respect to second layer weights
    dW3 = 1/m*(a2.T).dot(dz3)
    dW2 = 1/m*(a1.T).dot(dz2)
    # Calculate loss derivative with respect to second layer bias
    db3 = 1/m*np.sum(dz3, axis=0)
    # Calculate loss derivative with respect to first layer
    dz2 = np.multiply(dz3.dot(W3.T), tanh_derivative(a2))
    # Calculate loss derivative with respect to first layer weights
    dW2 = 1/m*np.dot(a1.T, dz2)
    # Calculate loss derivative with respect to first layer bias
    db2 = 1/m*np.sum(dz2, axis=0)
    dz1 = np.multiply(dz2.dot(W2.T), tanh_derivative(a1))
    dW1 = 1/m*np.dot(a0.T, dz1)
    db1 = 1/m*np.sum(dz1, axis=0)
    # Store gradients
    grads = {'dW3': dW3, 'db3': db3, 'dW2': dW2,
             'db2': db2, 'dW1': dW1, 'db1': db1}
    return grads


# This is what we return at the
ndmodel = initialise_parameters(nn_input_dim=13, nn_hdim=5, nn_output_dim=3)
model = train(model, X, y, learning_rate=0.07, epochs=4500, print_loss=True)
plt.plot(losses)
