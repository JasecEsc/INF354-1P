#normalizacion
import pandas as pd
from google.colab import drive
from sklearn.preprocessing import MinMaxScaler

drive.mount("/content/drive")
archivo = "/content/drive/My Drive/data/lifedata.csv"
dataset = pd.read_csv(archivo)

nume = ['Life Expectancy', 'Population', 'CO2 emissions', 'Health expenditure', 'Electric power consumption',
                      'Forest area', 'GDP per capita', 'Individuals using the Internet', 'Military expenditure',
                      'People practicing open defecation', 'People using at least basic drinking water services',
                      'Obesity among adults', 'Beer consumption per capita']


scaler = MinMaxScaler()
dataset[nume] = scaler.fit_transform(dataset[nume])
print(dataset)