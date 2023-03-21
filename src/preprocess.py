import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import sys

# input_file = sys.argv[1]
# output_file = sys.argv[2]

# def read_data(path):
df = pd.read_csv('./data/mushrooms.csv')

# create a LabelEncoder object
le = LabelEncoder()

# label encode columns
df = df.apply(le.fit_transform)

# Split the data
X = df.drop('class', axis=1)
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
df.to_csv('./data/prepared/mushrooms_prepared.csv', index=False)

    # return X_train, X_test, y_train, y_test

