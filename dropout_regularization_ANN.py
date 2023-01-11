import numpy as np
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow import keras

warnings.filterwarnings('ignore')

df = pd.read_csv("./sonar_dataset.csv", header = None)
df.isna().sum()
df.columns
df[60].value_counts()
X = df.drop(60, axis = 1)
y = df[60]
y = pd.get_dummies(y, drop_first = True)
y.value_counts()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 1)

# Model without Dropout Layer
model = keras.Sequential([
    keras.layers.Dense(60, input_dim = 60, activation = 'relu'),
    keras.layers.Dense(30, activation = 'relu'),
    keras.layers.Dense(15, activation = 'relu'),
    keras.layers.Dense(1, activation = 'sigmoid')
])

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.fit(X_train, y_train, epochs = 500, batch_size = 8)
model.evaluate(X_test, y_test)

y_pred = model.predict(X_test).reshape(-1)

# round the values to nearest integer ie 0 or 1
y_pred = np.round(y_pred)

y_test[:10]
print('Model without Dropout Layer\n' + classification_report(y_test, y_pred))

# Model with Dropout Layer
modeld = keras.Sequential([
    keras.layers.Dense(60, input_dim = 60, activation = 'relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(30, activation = 'relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(15, activation = 'relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(1, activation = 'sigmoid')
])

modeld.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
modeld.fit(X_train, y_train, epochs = 500, batch_size = 8)
modeld.evaluate(X_test, y_test)

y_pred_drop = modeld.predict(X_test).reshape(-1)

y_pred_drop = np.round(y_pred_drop)

print('Model with Dropout Layer\n' + classification_report(y_test, y_pred_drop))