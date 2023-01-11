import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

(X_train, y_train) , (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train / 255
X_test = X_test / 255
X_train_flattened = X_train.reshape(-1, 28, 28, 1)
X_test_flattened = X_test.reshape(-1, 28, 28, 1)

cnn = keras.Sequential([
    keras.layers.Conv2D(30, (3, 3), activation = 'relu', input_shape = (28, 28, 1)),
    keras.layers.MaxPooling2D((2, 2)),

    keras.layers.Flatten(),
    keras.layers.Dense(100, activation = 'relu'),
    keras.layers.Dense(10, activation = 'softmax')
])

cnn.compile(optimizer = 'adam',
            loss = 'sparse_categorical_crossentropy',
            metrics = ['accuracy'])

cnn.fit(X_train_flattened, y_train, epochs = 5)
cnn.evaluate(X_test_flattened, y_test)
y_pred = cnn.predict(X_test_flattened)
y_classes = [np.argmax(element) for element in y_pred]
cm = tf.math.confusion_matrix(labels = y_test, predictions = y_classes)

'''plt.figure(figsize = (10,7))
sn.heatmap(cm, annot = True, fmt = 'd')
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()'''

def plot_sample(X, y, index):
    plt.figure(figsize = (1, 2))
    plt.imshow(X[index])
    plt.xlabel(y[index])
    plt.show()

plot_sample(X_test, y_test, 10)
print(y_classes[10])