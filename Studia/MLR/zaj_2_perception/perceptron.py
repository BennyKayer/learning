'''
Plik zawiera szkielet programu, który definiuje i trenuje perceptron prosty.

Uzupełnić program o:
- wczytanie danych treningowych z pliku CSV,
- zainicjowanie wag losowymi wartościami,
- przeprowadzenie treningu perceptronu metodą gradientową,
- przeprowadzenie testu perceptronu.

Program należy wykorzystać do nauczenia perceptronu dodawania w zakresie [0,1].
'''
from pathlib import Path
import numpy as np


def f(x):
    '''
    Hyperbolic tangent
    '''
    return float(np.tanh(x))


def fprim(x):
    '''
    Derivative to the hyperbolic tangent
    '''
    return float(1 - np.tanh(x) ** 2)


def read_input_data(filename):
    '''
    Reads input data (train / test) from a CSV file.
    Input:
        filename - CSV file name (string)
    CSV file format:  
        input1, input2, ..., output
                        ...
                        ...  
    Returns: 
        Nin - number of inputs of the perceptron (int)
        X - input training data (list)
        Y - output (expected) training data (list)
    '''
    import csv
    Nin = 2
    X = []
    Y = []
    file = open(filename, "r")
    # bez tego trzeba przerabiac float'em
    data = csv.reader(file, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    for line in data:
        X.append(line[0:Nin])
        Y.append(line[Nin])  # patrz na tabelke
    file.close()

    return Nin, X, Y


def initialize_weights(Nin):
    '''
    Initialize weights with a random numbers from range [0,1).
    Input:
        Nin - number of inputs of the perceptron (int)
    Output:
        Randomly initialized weights (list of Nin size)
    '''
    import random
    w = [random.random() for x in range(Nin)]
    return w


def train(epochs, X, Y, weights, eta):
    '''
    Trains the simple perceptron using the gradient method.
    Plots the RMSE.
    Inputs:
        epochs - number of training iterations (int > 0)
        X - training (input) vector (list)
        Y - training (output) vector (list)
        weights - initial weights (list)
        eta - learning rate (0-1]
    Returns:
        weights - optimized weights (list)
    Pseudo code:
        For each epoch:
          For each training data (pair X,Y):
              Calculate output Yout
              Use Yout to calculate error
              Adjust weights using the gradient formula
              Calculate ans store the RMSE (root mean squared error)
        Plot the RMSE(epoch)
    '''

    rms_errors = []
    for i in range(epochs):
        rms_error = 0.0
        for j in range(len(X)):
            sumWeighted = 0.0
            for k in range(Nin):
                sumWeighted += float(weights[k] * X[j][k])
            Yout = f(sumWeighted)
            rms_error = float((Yout - Y[j]) ** 2)
            for l in range(len(weights)):
                current_x = float(X[j][l])
                difference_y = float(Y[j] - Yout)
                derivative = fprim(f(sumWeighted))
                weights[l] += eta * current_x * difference_y * derivative
        rms_errors.append(rms_error / len(X))
    import matplotlib.pyplot as plt
    plt.plot(rms_errors)
    plt.show()
    return weights


def test(filename, weights):
    '''
    Test ot the trained perceptron by propagating the test data.
    Input:
        filename - CSV file name (string)
        weights - trained weights (list)
    CSV file format:  
        input1, input2, ..., expected_output
                        ...
                        ...  
    Returns: 
        Y - output testing results (list)
        Yexpected - output expected results (list)

    '''

    Y = []
    Nin, Xtest, Yexpected = read_input_data(filename)
    for i in range(len(Xtest)):
        sumWeighted = 0
        for j in range(Nin):
            sumWeighted += weights[j] * Xtest[i][j]
        Y.append(f(sumWeighted))
    return Y, Yexpected


if __name__ == '__main__':
    '''
     Simple perceptron

                 Yout
                  ^
                  |
                  O
                / | \         weights: weights[]
              Nin inputs
    '''
    data_folder = Path("data")
    train_data = data_folder / "train_data.csv"
    test_data = data_folder / "test_data.csv"

    # Get the train data
    Nin, Xtrain, Ytrain = read_input_data(train_data)

    print(Nin, Xtrain, Ytrain)
    # Initialize weights
    weights = initialize_weights(Nin)
    print(weights)

    # Train of the perceptron
    epochs = 100
    eta = 0.15
    weights = train(epochs, Xtrain, Ytrain, weights, eta)

    # Test of the perceptron with the trained weights
    Yout, Yexpected = test(test_data, weights)
    print("Results:", Yout)
    print("Expected results:", Yexpected)
