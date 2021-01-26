import tensorflow as tf
import tensorflow.keras as keras
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

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

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
h = model.fit(x=x_train, y=y_train, epochs=epoch, batch_size=128, validation_split=0.2, verbose=1)

model.save('mnist.h5')

test_score = model.evaluate(x_test, y_test, verbose=0)

print(f"Loss {test_score[0]}, accuracy {test_score[1]*100}%")

errs = {
    
}

y_pred =  model.predict(x_test)
for i in range(len(y_pred)):
    pred = np.argmax(y_pred[i])
    test = np.argmax(y_test[i])
    if (pred != test):
        print(f"{i+1}. {pred} : {test}")
        if (pred, test) in errs.keys():
            errs[(pred, test)] += 1
        else:
            errs[(pred, test)] = 1

errs = {k: v for k, v in sorted(errs.items(), key=lambda item: item[1], reverse=True)}
for d_i in errs.items():
    print(d_i)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(range(epoch), h.history["loss"])
plt.plot(range(epoch), h.history["val_loss"])
plt.plot(range(epoch), h.history["accuracy"])
plt.plot(range(epoch), h.history["val_accuracy"])
plt.savefig("mnist.png")

#zad dodatkowe - zrob to samo na zwyklej sieci i porownaj