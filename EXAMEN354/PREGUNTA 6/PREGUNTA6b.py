#codificación de etiquetas (Label Encoding), que asigna un valor numerico a cada categoria unica
import pandas as pd
from google.colab import drive
from sklearn.preprocessing import LabelEncoder

drive.mount("/content/drive")
archivo = "/content/drive/My Drive/data/lifedata.csv"
dataset = pd.read_csv(archivo)
label_en = {}
categorical_columns = ['Country', 'Continent', 'Least Developed']

for col in categorical_columns:
    le = LabelEncoder()
    dataset[col] = le.fit_transform(dataset[col])
    label_en[col] = le

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(dataset)
