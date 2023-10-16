#Generacion de caracteristicas: Caracteristicas basadas en rangos
import pandas as pd
from google.colab import drive

drive.mount("/content/drive")
archivo = "/content/drive/My Drive/data/lifedata.csv"
dataset = pd.read_csv(archivo)

bins = [0, 1000, 10000, 50000, float("inf")]
labels = ['Muy Bajo', 'Bajo', 'Medio', 'Alto']

dataset['GDP Range'] = pd.cut(dataset['GDP per capita'], bins=bins, labels=labels, right=False)

print(dataset[['Country', 'GDP per capita', 'GDP Range']])