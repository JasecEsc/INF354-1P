import pandas as pd
from google.colab import drive

drive.mount("/content/drive")
archivo = "/content/drive/My Drive/data/lifedata.csv"
dataset = pd.read_csv(archivo)

# Mapear los continentes a valores binarios
continent_mapping = {
    'Africa': '000001',
    'Asia': '000010',
    'Europe': '000100',
    'North America': '001000',
    'Oceania': '010000',
    'South America': '100000'
}
# Mapear los valores "TRUE" y "FALSE" a 1 y 0
dataset['Least Developed'] = dataset['Least Developed'].map({True: 1, False: 0})

# Reemplazar la columna original "Continent" con los valores binarios
dataset['Continent'] = dataset['Continent'].map(continent_mapping)
print(dataset)