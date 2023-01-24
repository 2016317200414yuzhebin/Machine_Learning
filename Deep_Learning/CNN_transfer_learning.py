import numpy as np
import cv2
import PIL

import PIL.Image as Image
import os

import matplotlib.pylab as plt

import tensorflow as tf
import tensorflow_hub as hub

from tensorflow import keras

import pathlib
from sklearn.model_selection import train_test_split

IMAGE_SHAPE = (224, 224)

classifier = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4", input_shape = IMAGE_SHAPE+(3,))
])

gold_fish = Image.open("goldfish.jpg").resize(IMAGE_SHAPE)
gold_fish = np.array(gold_fish) / 255.0

result = classifier.predict(gold_fish[np.newaxis, ...])
predicted_label_index = np.argmax(result)
image_labels = []
with open("ImageNetLabels.txt", "r") as f:
    image_labels = f.read().splitlines()

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos', origin = dataset_url, cache_dir = '.', untar = True)

data_dir = pathlib.Path(data_dir)

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

img = cv2.imread(str(flowers_images_dict['roses'][0]))
cv2.resize(img,(224,224)).shape

X, y = [], []

for flower_name, images in flowers_images_dict.items():
    for image in images:
        img = cv2.imread(str(image))
        resized_img = cv2.resize(img, (224,224))
        X.append(resized_img)
        y.append(flowers_labels_dict[flower_name])

X = np.array(X)
y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)
X_train_scaled = X_train / 255
X_test_scaled = X_test / 255

IMAGE_SHAPE+(3,)
x0_resized = cv2.resize(X[0], IMAGE_SHAPE)
x1_resized = cv2.resize(X[1], IMAGE_SHAPE)
x2_resized = cv2.resize(X[2], IMAGE_SHAPE)

plt.axis('off')
plt.imshow(X[2])
plt.show()

predicted = classifier.predict(np.array([x0_resized, x1_resized, x2_resized]))
predicted = np.argmax(predicted, axis = 1)

# take pre-trained model and retrain it using flowers images
feature_extractor_model = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"

pretrained_model_without_top_layer = hub.KerasLayer(
    feature_extractor_model, input_shape = (224, 224, 3), trainable = False)

num_of_flowers = 5

model = tf.keras.Sequential([
  pretrained_model_without_top_layer,
  tf.keras.layers.Dense(num_of_flowers)
])

model.summary()

model.compile(
  optimizer = "adam",
  loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),
  metrics = ['acc'])

model.fit(X_train_scaled, y_train, epochs = 10)
model.evaluate(X_test_scaled, y_test)
y_pred = model.predict(X_test_scaled)
y_classes = [np.argmax(element) for element in y_pred]

flowers_names_dict = {v : k for k, v in flowers_labels_dict.items()}

def plot_sample(X, y, index):
    plt.figure(figsize = (1, 2))
    plt.imshow(X[index])
    plt.xlabel(flowers_names_dict[y[index]])
    plt.show()

num = 0

while num >= 0:
    num = int(input("请输入数字："))
    if num >= 0:
        plot_sample(X_test_scaled, y_test, num)
        print('correct answer: ' + flowers_names_dict[y_test[num]] + '\nprediction: ' + flowers_names_dict[y_classes[num]])