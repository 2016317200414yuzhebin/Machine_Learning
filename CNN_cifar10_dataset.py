import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

(X_train, y_train), (X_test,y_test) = tf.keras.datasets.cifar10.load_data()

# y_train is a 2D array, for our classification having 1D array is good enough. so we will convert this to now 1D array
y_train = y_train.reshape(-1,)
y_test = y_test.reshape(-1,)
X_train = X_train / 255.0
X_test = X_test / 255.0

classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

def plot_sample(X, y, index):
    plt.figure(figsize = (1, 2))
    plt.imshow(X[index])
    plt.xlabel(classes[y[index]])
    plt.show()

plot_sample(X_train, y_train, 0)

# ANN
'''
ann = keras.models.Sequential([
        keras.layers.Flatten(input_shape = (32, 32, 3)),
        keras.layers.Dense(3000, activation = 'relu'),
        keras.layers.Dense(1000, activation = 'relu'),
        keras.layers.Dense(10, activation = 'softmax')    
    ])

ann.compile(optimizer = 'SGD',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

ann.fit(X_train, y_train, epochs = 5)

y_pred = ann.predict(X_test)
y_pred_classes = [np.argmax(element) for element in y_pred]
print("Classification Report: \n", classification_report(y_test, y_pred_classes))
'''

# CNN
cnn = keras.models.Sequential([
    keras.layers.Conv2D(filters = 32, kernel_size = (3, 3), activation = 'relu', input_shape = (32, 32, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    
    keras.layers.Conv2D(filters = 64, kernel_size = (3, 3), activation = 'relu'),
    keras.layers.MaxPooling2D((2, 2)),
    
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation = 'relu'),
    keras.layers.Dense(10, activation = 'softmax')
])

cnn.compile(optimizer = 'adam',
            loss = 'sparse_categorical_crossentropy',
            metrics = ['accuracy'])

cnn.fit(X_train, y_train, epochs = 10)
cnn.evaluate(X_test, y_test)
y_pred = cnn.predict(X_test)
y_classes = [np.argmax(element) for element in y_pred]
plot_sample(X_test, y_test, 5)
print(classes[y_classes[5]])