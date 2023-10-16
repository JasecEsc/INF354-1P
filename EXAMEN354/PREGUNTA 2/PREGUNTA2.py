import numpy as np
import pandas as pd

archivo = r"C:\Users\Desktop\Desktop\EXAMEN354\Life_Expectancy_00_15.csv"
df = pd.read_csv(archivo)

columnas_especificadas = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

medias = df.iloc[:, columnas_especificadas].mean()
print("Medias de las columnas:")
print(medias)

modas = df.iloc[:, columnas_especificadas].mode().iloc[0]
print("\nModas de las columnas:")
print(modas)

percentiles = [25, 50, 75]
cuantiles = df.iloc[:, columnas_especificadas].quantile([p / 100 for p in percentiles])
print("\nCuartiles y percentiles de las columnas:")
print(cuantiles)
