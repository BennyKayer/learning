import numpy as np

A = [1, 2, 3, 4, 5, 6]
B = [-1, -2, -3, -4, -5, -6]
C = [2, 3, 4, 5, 6, 7]

# will print weird numbers
print(np.correlate(A, B))
print(np.correlate(B, C))

# we have to make it readable


def correlate_normalize(a, b):
    a = (a - np.mean(a)) / (np.std(a) * len(a))
    b = (b - np.mean(b)) / (np.std(b))
    return np.correlate(a, b)


print(correlate_normalize(A, B))
print(correlate_normalize(A, C))
