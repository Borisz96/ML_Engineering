import pandas as pd

df = pd.read_csv('./data/mushrooms.csv')
print(len(df.columns))