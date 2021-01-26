import numpy as np


def sigmoid(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input data
X = np.array([
    [0.2, 0.2],
    [0.1, 0.3],
    [0.5, 0.1],
    [0.8, 0.2],
    [0.5, 0.3]
])
# output data
Y = np.array([
    [0.4],
    [0.4],
    [0.6],
    [1.0],
    [0.8]
])
np.random.seed(1)

# synapses or weights
syn0 = np.random.rand(2, 5)
syn1 = np.random.rand(5, 1)

print(syn0)
print(syn1)

# training step
for j in range(60000):
    l0 = X
    l1 = sigmoid(np.dot(l0, syn0))
    l2 = sigmoid(np.dot(l1, syn1))

    l2_error = Y - l2

    if(j % 10000) == 0:
        print(f"Error: {str(np.mean(np.abs(l2_error)))}")

    l2_delta = l2_error * sigmoid(l2, deriv=True)

    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * sigmoid(l1, deriv=True)

    # update weights
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print("Output after training")
print(l2)
