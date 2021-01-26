from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from pathlib import Path

# All three columns from csv
folder = Path("zaj_5_6_7_keras_tf")
dataset = np.loadtxt(folder / "train_data.csv", delimiter=',')
# First two are the numbers to add the last one contains answers
X = dataset[:, 0:2]
Y = dataset[:, 2:]
# Split X and Y so that 70% of the dataset is train and the rest is test
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, train_size=0.7, random_state=42)
# print("X_train", X_train)
# print("X_test", X_test)
# print("Y_train", Y_train)
# print("Y_test", Y_test)

model = Sequential()
model.add(Dense(10, input_dim=2, activation="relu"))
model.add(Dense(5, activation="tanh"))
model.add(Dense(1, activation="hard_sigmoid"))

model.compile(loss="mean_squared_error", optimizer="adam")

history = model.fit(X_train, Y_train, epochs=1000,
                    validation_data=(X_test, Y_test), verbose=1)

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title("Model Accuracy")
plt.ylabel("Loss / Validation")
plt.xlabel("Epoch")
plt.legend(['Train', 'Test'], loc="upper right")
plt.savefig("plot.png")
plt.show()

model.save("summation_10k")
