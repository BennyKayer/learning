import numpy as np
import math
from pathlib import Path
'''
Implementing Neural Network from scratch
'''


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork:
    '''
    activation_function as act_f => normalizes input so it's easier to say whether the neuron should fire
    input_layer as x => 
    weights_input_to_hidden as weights_1 => 
    hidden_layer as y =>
    weights_hidden_to_output as weights_2 => 
    output_layer as y_exp =>
    loss_function as loss_f =>
    '''

    def __init__(self, x, y):
        self.x = x
        self.weights_1 = np.random.rand(self.x.shape[1], 4)
        print(self.x)
        print(self.weights_1)
        self.y = y
        self.weights_2 = np.random.rand(4, 1)

        self.y_exp = np.zeros(y.shape)

    def feedforward(self):
        '''
        Formula => 
            inner = act_f(x * weights_1 + bias_input)
            y_exp = act_f(y * inner + bias_hidden)
        '''
        self.layer1 = sigmoid(np.dot(self.x, self.weights_1))
        self.y_exp = sigmoid(np.dot(self.layer1, self.weights_2))

    def backpropagation(self):
        '''

        '''
        d_weight_2 = np.dot(
            self.layer1.T, (2 * (self.y - self.y_exp) * sigmoid_derivative(self.y_exp)))
        d_weights1 = np.dot(self.x.T,  (np.dot(2*(self.y - self.y_exp) * sigmoid_derivative(
            self.y), self.weights_2.T) * sigmoid_derivative(self.layer1)))

        self.weights_1 += d_weights1
        self.weights_2 += d_weight_2


if __name__ == "__main__":
    # input_neurons = int(input(" How many input neurons?: "))
    # hidden_neurons = int(input(" How many hidden neurons?: "))
    # output_neurons = int(input(" How many output neurons?: "))
    # input data
    X = np.array([
        [0.2, 0.2],
        [0.1, 0.3],
        [0.5, 0.1],
        [0.8, 0.2],
    ])
    # output data
    Y = np.array([
        [0.4],
        [0.4],
        [0.6],
        [1.0],
    ])
    nt = NeuralNetwork(X, Y)
    nt.feedforward()
