import numpy as np
import random

n_layers = int(input("Enter # of layers: "))

n_hidden = n_layers
n_in = n_layers
n_out = n_layers

# hyperparameters
learning_rate = 0.01
momentum = 0.9


def generate_data(n_data):
    X = []
    Y = []
    for i in range(n_data):
        a = 1
        b = 1
        while a + b > 1.0:
            a = random.random()
            b = random.random()
        X.append([a, b])
        Y.append(a + b)
    X = np.array(X)
    Y = np.array(Y)
    return X, Y


def tanh(x, deriv=False):
    if deriv:
        return 1 - np.tanh(x) ** 2
    return np.tanh(x)


def train(x, y, V, W, bv, bw):
    '''
    x - input layer
    y - expected output
    V, W - layers
    bv, bw - biases
    '''
    # forward prop dot + biases
    A = np.dot(x, V) + bv
    Z = np.tanh(A)

    B = np.dot(Z, W) + bw
    Y = tanh(B)

    # backward prop
    Ew = Y - y
    Ev = tanh(A, deriv=True) * np.dot(W, Ew)

    # predict loss
    dW = np.outer(Z, Ew)
    dV = np.outer(x, Ev)

    # cross entropy - loss function
    loss = -np.mean(y * np.log(Y) + (1 - y) * np.log(1 - Y))

    return loss, (dV, dW, Ev, Ew)


def predict(x, V, W, bv, bw):
    A = np.dot(x, V) + bv
    B = np.dot(np.tanh(A), W) + bw
    return tanh(B)


# create layers
V = np.random.normal(scale=0.1, size=(n_in, n_hidden))
W = np.random.normal(scale=0.1, size=(n_hidden, n_out))

bv = np.zeros(n_hidden)
bw = np.zeros(n_out)

params = [V, W, bv, bw]

X, Y = generate_data(10)

# train time
for epoch in range(100):
    err = []
    upd = [0] * len(params)

    for i in range(len(X.shape)):
        loss, grad = train(X[i], Y[i], *params)
        for j in range(len(params)):
            params[j] -= upd[j]
        for j in range(len(params)):
            upd[j] = learning_rate * grad[j] + momentum * upd[j]

        err.append(loss)

    print(f'Epoch: {epoch}, Loss: {np.mean(err)}')

# try to predict
x = generate_data(10)
print(x)
print(predict(x, *params))
