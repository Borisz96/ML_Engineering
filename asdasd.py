import pandas as pd

df = pd.read_csv('./data/mushrooms.csv')

df_shape = df.shape[1]
df_columns = df.columns
print(df.columns)

