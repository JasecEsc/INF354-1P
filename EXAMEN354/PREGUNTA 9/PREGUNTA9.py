import random
from sklearn.datasets import load_iris

datos = load_iris()
caract = datos.data
etiq = datos.target

datos_etiq = list(zip(caract, etiq))
random.shuffle(datos_etiq)
caract, etiq = zip(*datos_etiq)

total_muestras = len(caract)
tam_entrenamiento = int(0.8 * total_muestras)  
tam_prueba = total_muestras - tam_entrenamiento  

entrenamiento_caract = caract[:tam_entrenamiento]
entrenamiento_etiq = etiq[:tam_entrenamiento]
prueba_caract = caract[tam_entrenamiento:]
prueba_etiq = etiq[tam_entrenamiento:]
#hacer correr con python PREGUNTA9.py
print("Tamaño del conjunto de entrenamiento:", len(entrenamiento_caract))
print("Tamaño del conjunto de prueba:", len(prueba_caract))
