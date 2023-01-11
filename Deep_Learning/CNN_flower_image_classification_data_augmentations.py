import matplotlib.pyplot as plt
import numpy as np
import cv2
import PIL
import tensorflow as tf
from tensorflow import keras
import pathlib
from sklearn.model_selection import train_test_split

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos', origin = dataset_url,  cache_dir = '.', untar = True)
data_dir = pathlib.Path(data_dir)
# list(data_dir.glob('*/*.jpg'))[:5]
image_count = len(list(data_dir.glob('*/*.jpg')))
roses = list(data_dir.glob('roses/*'))
PIL.Image.open(str(roses[1]))
# tulips = list(data_dir.glob('tulips/*'))
# PIL.Image.open(str(tulips[0]))

flowers_images_dict = {
    'roses': list(data_dir.glob('roses/*')),
    'daisy': list(data_dir.glob('daisy/*')),
    'dandelion': list(data_dir.glob('dandelion/*')),
    'sunflowers': list(data_dir.glob('sunflowers/*')),
    'tulips': list(data_dir.glob('tulips/*')),
}
flowers_labels_dict = {
    'roses': 0,
    'daisy': 1,
    'dandelion': 2,
    'sunflowers': 3,
    'tulips': 4,
}

# img = cv2.imread(str(flowers_images_dict['roses'][0]))
# cv2.resize(img, (180, 180))

X, y = [], []

for flower_name, images in flowers_images_dict.items():
    for image in images:
        img = cv2.imread(str(image))
        resized_img = cv2.resize(img, (180, 180))
        X.append(resized_img)
        y.append(flowers_labels_dict[flower_name])

X = np.array(X)
y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
X_train_scaled = X_train / 255
X_test_scaled = X_test / 255

num_classes = len(flowers_labels_dict)

'''
model = keras.Sequential([
    keras.layers.Conv2D(16, 3, padding = 'same', activation = 'relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(32, 3, padding = 'same', activation = 'relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64, 3, padding = 'same', activation = 'relu'),
    keras.layers.MaxPooling2D(),

    keras.layers.Flatten(),
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(num_classes)
])

model.compile(optimizer = 'adam',
              loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics = ['accuracy'])
              
model.fit(X_train_scaled, y_train, epochs = 30)
model.evaluate(X_test_scaled, y_test)
predictions = model.predict(X_test_scaled)

score = tf.nn.softmax(predictions[0])
# np.argmax(score)
# y_test[0]
'''

# use data augmentation to address overfitting
data_augmentation = keras.Sequential([
    keras.layers.experimental.preprocessing.RandomFlip("horizontal", input_shape = (180, 180, 3)),
    keras.layers.experimental.preprocessing.RandomRotation(0.1),
    keras.layers.experimental.preprocessing.RandomZoom(0.1),
])

# Original Image
plt.axis('off')
plt.imshow(X[0])
plt.show()

# Newly generated training sample using data augmentation
plt.axis('off')
plt.imshow(data_augmentation(X)[0].numpy().astype("uint8"))
plt.show()

model = keras.Sequential([
    data_augmentation,
    keras.layers.Conv2D(16, 3, padding = 'same', activation = 'relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(32, 3, padding = 'same', activation = 'relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64, 3, padding = 'same', activation = 'relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Dropout(0.2),

    keras.layers.Flatten(),
    keras.layers.Dense(128, activation = 'relu'),
    keras.layers.Dense(num_classes)
])

model.compile(optimizer = 'adam',
              loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics = ['accuracy'])
              
model.fit(X_train_scaled, y_train, epochs = 30)
model.evaluate(X_test_scaled, y_test)
y_pred = model.predict(X_test_scaled)
y_classes = [np.argmax(element) for element in y_pred]

def plot_sample(X, y, index):
    plt.figure(figsize = (1, 2))
    plt.imshow(X[index])
    plt.xlabel(y[index])
    plt.show()

flowers_names_dict = {v : k for k, v in flowers_labels_dict.items()}

plot_sample(X_test_scaled, y_test, 7)
print('correct answer: ' + flowers_names_dict[y_test[7]] + '\nprediction: ' + flowers_names_dict[y_classes[7]])