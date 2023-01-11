from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Flatten, Dense

(X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()
X_train = X_train/255
X_test = X_test/255

model = keras.Sequential()
model.add(Flatten(input_shape = [28, 28]))
model.add(Dense(100, activation = "relu"))
model.add(Dense(10, activation = "softmax"))
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X_train, y_train)
model.evaluate(X_test, y_test)

plt.matshow(X_test[2])
plt.show()

yp = model.predict(X_test)
class_labels = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
print(class_labels[np.argmax(yp[2])])