import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import pathlib

IMAGE_SIZE = 100

class Monster_Classification:
    def get_data(self, data_dir):
        path_dir = pathlib.Path(data_dir)
        directory = [var for var in os.listdir(data_dir)]
        X, y = [], []
        monsters_images_dict = {}
        monsters_labels_dict = {}

        for index, monster in enumerate(directory):
            images_path = monster + '/*'
            monsters_images_dict[monster] = list(path_dir.glob(images_path))
            monsters_labels_dict[monster] = index

        for monster_name, images in monsters_images_dict.items():
            for image in images:
                img = cv2.imread(str(image)) # convert BGR to RGB format
                resized_img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE)) # Reshaping images to preferred size
                X.append(resized_img)
                y.append(monsters_labels_dict[monster_name])
        
        num_classes = len(monsters_labels_dict)
        
        return np.array(X), np.array(y), num_classes
    
    def monsters_model(self, X_train, y_train, X_test, y_test, num_classes, epochs = 50):
        # use data augmentation to address overfitting
        data_augmentation = keras.Sequential([
            keras.layers.experimental.preprocessing.RandomFlip("horizontal", input_shape = (IMAGE_SIZE, IMAGE_SIZE, 3)),
            keras.layers.experimental.preprocessing.RandomRotation(0.1),
            keras.layers.experimental.preprocessing.RandomZoom(0.1),
        ])

        model = keras.Sequential([
            data_augmentation,
            
            keras.layers.Conv2D(32, 3, padding = 'same', activation = 'relu'),
            keras.layers.MaxPooling2D(),
            
            keras.layers.Conv2D(32, 3, padding = 'same', activation = 'relu'),
            keras.layers.MaxPooling2D(),
            keras.layers.Dropout(0.5),
            
            keras.layers.Conv2D(64, 3, padding = 'same', activation = 'relu'),
            keras.layers.MaxPooling2D(),
            keras.layers.Dropout(0.5),

            keras.layers.Flatten(),
            keras.layers.Dense(128, activation = 'relu'),
            keras.layers.Dense(num_classes, activation = "softmax")
        ])
        
        model.compile(optimizer = 'adam',
                loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
                metrics = ['accuracy'])
        
        # model.fit(X_train, y_train, epochs)
        # model.evaluate(X_test, y_test)
        history = model.fit(X_train, y_train, epochs = epochs, validation_data = (X_test, y_test))
        model.save('../Result/model/model.hdf5')
        return history

if __name__ == '__main__':
    train_dir = '../Data/train'
    test_dir = '../Data/test'

    m = Monster_Classification()

    X, y, train_class = m.get_data(train_dir)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
    X_train_scaled = X_train / 255
    X_test_scaled = X_test / 255
    # X_train_scaled = X_train_scaled.reshape(-1, IMAGE_SIZE, IMAGE_SIZE, 1)
    # X_test_scaled = X_test_scaled.reshape(-1, IMAGE_SIZE, IMAGE_SIZE, 1)

    history = m.monsters_model(X_train_scaled, y_train, X_test_scaled, y_test, train_class, 50)
    
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
 
    epochs_range = range(50)
 
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label = 'Training Accuracy')
    plt.plot(epochs_range, val_acc, label = 'Validation Accuracy')
    plt.legend(loc = 'lower right')
    plt.title('Training and Validation Accuracy')
 
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label = 'Training Loss')
    plt.plot(epochs_range, val_loss, label = 'Validation Loss')
    plt.legend(loc = 'upper right')
    plt.title('Training and Validation Loss')

    plt.savefig('../Result/plot/result_2.jpg', bbox_inches='tight')
    plt.show()