import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
import sys

model_file = sys.argv[1]
input_file = sys.argv[2]

with open(model_file, 'rb') as f:
    model = pickle.load(f)
df = pd.read_csv(input)