#se eliminaron algunas celdas para realizar la imputacion
from google.colab import drive
drive.mount("/content/drive")

archivo = "/content/drive/My Drive/data/lifedata_imputacion.csv"

datos = []
with open(archivo, 'r') as f:
    next(f)

    for linea in f:
        fila = linea.strip().split(',')
        datos.append(fila)

for fila in datos:
    for i in range(len(fila)):
        try:
            fila[i] = float(fila[i])
        except ValueError:
            pass  


columnas_especificas = [1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

for columna in columnas_especificas:
    valores_columna = [fila[columna] for fila in datos if not isinstance(fila[columna], str)]
    suma_columna = sum(valores_columna)
    contador_columna = len(valores_columna)
    if contador_columna > 0:
        media_columna = suma_columna / contador_columna
        for fila in datos:
            if isinstance(fila[columna], str):
                fila[columna] = media_columna


formato_decimal = "{:.6f}"
datos_formateados = [[formato_decimal.format(valor) if isinstance(valor, float) else valor for valor in fila] for fila in datos]


for fila in datos_formateados:
    print(','.join(map(str, fila)))