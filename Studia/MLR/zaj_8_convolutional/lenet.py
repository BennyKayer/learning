import keras
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# mapa i cyferka
# print(x_train[0], y_train[0])

# Normalize
x_train = x_train.astype('float32')
y_train = y_train.astype("float32")

# print(x_train[0], y_train[0])

x_train = [x / 255 for x in x_train]
x_test =[x / 255 for x in x_test]

# print(x_train[0], x_test[0])

y_train = keras.utils.np_utils.to_categorical(y_train, 10)
y_test = keras.utils.np_utils.to_categorical(y_test, 10)

# print(x_train[0], y_train[0])

x_train = np.array(x_train)
x_test = np.array(x_test)

x_train = np.reshape(x_train, (list(x_train.shape)[0], 28, 28, 1))
x_test = np.reshape(x_test,(list(x_test.shape)[0], 28, 28, 1))

model = keras.models.Sequential()

model.add(keras.layers.Conv2D(6, kernel_size = (5, 5), strides = (1,1), activation = "tanh", input_shape=(28, 28, 1), padding="same"))

model.add(keras.layers.AveragePooling2D(pool_size=(2,2), strides=(2,2), padding="valid"))

model.add(keras.layers.Conv2D(16, kernel_size=(5,5), strides=(1,1), activation="tanh", padding="valid"))

model.add(keras.layers.AveragePooling2D(pool_size=(2,2), strides=(2,2), padding="valid"))

model.add(keras.layers.Conv2D(120, kernel_size=(5,5), strides=(1,1), activation="tanh", padding="valid"))

model.add(keras.layers.Flatten())

model.add(keras.layers.Dense(84, activation="tanh"))

model.add(keras.layers.Dense(10, activation="softmax"))

model.compile(loss=keras.losses.categorical_crossentropy, optimizer="rmsprop", metrics = ['accuracy'])
model.summary()

epoch = 10
h = model.fit(x=x_train, y=y_train, epochs=epoch, batch_size=128, validation_split=0.2, verbose=0)

model.save('mnist.model')

test_score = model.evaluate(x_test, y_test)

print(f"Loss {test_score[0]}, accuracy {test_score[1]*100}%")

import matplotlib.pyplot as plt

plt.figure()
plt.plot(range(epoch), h.history["loss"], x_label="train loss")
plt.plot(range(epoch), h.history["val_loss"], x_label="val loss")
plt.plot(range(epoch), h.history["accuracy"], x_label="train accuracy")
plt.plot(range(epoch), h.history["val_accuracy"], x_label="validation accuracy")
plt.savefig("mnist.png")

#zad dodatkowe - zrob to samo na zwyklej sieci i porownaj