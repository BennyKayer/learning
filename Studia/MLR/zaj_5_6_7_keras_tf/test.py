from keras.models import load_model
import numpy as np
from pathlib import Path

folder = Path("zaj_5_6_7_keras_tf")
dataset = np.loadtxt(folder / "test_data.csv", delimiter=',')

X = dataset[:, 0:2]
Y = dataset[:, 2:]

model = load_model(folder / "summation_10k")

predictions = model.predict(X)

for i in range(len(Y)):
    print(X[i][0], X[i][1], predictions[i][0], Y[i])
