import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

df = pd.read_csv('Churn_Modelling.csv')
df.drop(['RowNumber', 'CustomerId', 'Surname'], axis = 'columns', inplace = True)

def print_unique_col_values(df):
    for column in df:
        if df[column].dtypes == 'object':
            print(f'{column}: {df[column].unique()}')

def ANN(X_train, y_train, X_test, y_test, loss):
    model = keras.Sequential([
        keras.layers.Dense(13, input_dim = 13, activation = 'relu'),
        keras.layers.Dense(10, activation = 'relu'),
        keras.layers.Dense(1, activation = 'sigmoid')
    ])

    model.compile(optimizer = 'adam', loss = loss, metrics = ['accuracy'])

    model.fit(X_train, y_train, epochs = 100)

    print(model.evaluate(X_test, y_test))

    y_preds = model.predict(X_test)
    y_preds = np.round(y_preds)

    print("Classification Report: \n", classification_report(y_test, y_preds))

    return y_preds

print_unique_col_values(df)

df1 = pd.get_dummies(data = df, columns = ['Geography', 'Gender'])

print_unique_col_values(df1)

scaler = MinMaxScaler()
col_to_scale = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
df1[col_to_scale] = scaler.fit_transform(df1[col_to_scale])

X = df1.drop('Exited', axis = 'columns')
y = df1.Exited
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 10, stratify = y)
y_preds = ANN(X_train, y_train, X_test, y_test, 'binary_crossentropy')

# Class count
count_class_0, count_class_1 = df1.Exited.value_counts()

# Divide by class
df_class_0 = df1[df1['Exited'] == 0]
df_class_1 = df1[df1['Exited'] == 1]

df_class_0_under = df_class_0.sample(count_class_1)
df_test_under = pd.concat([df_class_0_under, df_class_1], axis = 0)

print('Random under-sampling:\n' + df_test_under.Exited.value_counts())

X = df_test_under.drop('Exited', axis = 'columns')
y = df_test_under['Exited']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 15, stratify = y)
y_preds = ANN(X_train, y_train, X_test, y_test, 'binary_crossentropy')

# Oversample 1-class and concat the DataFrames of both classes
df_class_1_over = df_class_1.sample(count_class_0, replace = True)
df_test_over = pd.concat([df_class_0, df_class_1_over], axis = 0)

print('Random over-sampling:\n' + df_test_over.Exitedb.value_counts())

X = df_test_over.drop('Exited', axis = 'columns')
y = df_test_over['Exited']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 15, stratify = y)
y_preds = ANN(X_train, y_train, X_test, y_test, 'binary_crossentropy')

# SMOTE
X = df1.drop('Exited', axis = 'columns')
y = df1['Exited']
smote = SMOTE(sampling_strategy = 'minority')
X_sm, y_sm = smote.fit_resample(X, y)
X_train, X_test, y_train, y_test = train_test_split(X_sm, y_sm, test_size = 0.2, random_state = 15, stratify = y_sm)
y_preds = ANN(X_train, y_train, X_test, y_test, 'binary_crossentropy')

# Use of Ensemble with undersampling
X = df1.drop('Exited', axis = 'columns')
y = df1['Exited']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 15, stratify = y)
df2 = X_train.copy()
df2['Exited'] = y_train
df2_class0 = df2[df2.Exited == 0]
df2_class1 = df2[df2.Exited == 1]

def get_train_batch(df_majority, df_minority, start, end):
    df_train = pd.concat([df_majority[start:end], df_minority], axis = 0)

    X_train = df_train.drop('Exited', axis = 'columns')
    y_train = df_train.Exited
    return X_train, y_train

X_train, y_train = get_train_batch(df2_class0, df2_class1, 0, 1495)
y_pred1 = ANN(X_train, y_train, X_test, y_test, 'binary_crossentropy')

X_train, y_train = get_train_batch(df2_class0, df2_class1, 1495, 2990)
y_pred2 = ANN(X_train, y_train, X_test, y_test, 'binary_crossentropy')

X_train, y_train = get_train_batch(df2_class0, df2_class1, 2990, 4130)
y_pred3 = ANN(X_train, y_train, X_test, y_test, 'binary_crossentropy')

y_pred_final = y_pred1.copy()
for i in range(len(y_pred1)):
    n_ones = y_pred1[i] + y_pred2[i] + y_pred3[i]
    if n_ones > 1:
        y_pred_final[i] = 1
    else:
        y_pred_final[i] = 0

print('Use of Ensemble with undersampling\n' + classification_report(y_test, y_pred_final))