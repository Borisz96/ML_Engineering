import pandas as pd
from sklearn.model_selection import train_test_split
import sys

# input_file = sys.argv[1]
# output_file = sys.argv[2]

# def read_data(path):
df = pd.read_csv(path)
# Split the data
X = df.drop('class', axis=1)
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # return X_train, X_test, y_train, y_test

