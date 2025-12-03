import pandas as pd

df = pd.read_csv("./Data Potensi Pemain Basket.csv",delimiter=";")

df = df.drop("ID",axis=1) 
df = df.iloc[:, :-1]

print(df)

rows_with_nan = df[df.isna().any(axis=1)]

df.to_csv('Data Potensi Pemain Basket Tingkat SMA after preprocessing.csv', sep=';', index=False)