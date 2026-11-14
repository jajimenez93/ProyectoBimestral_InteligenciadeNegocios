import pandas as pd

inicio = pd.read_csv("datos/registro-administrativo-historico_2009-2024-inicio.csv", sep=";")

fin = pd.read_csv("datos/registro-administrativo-historico_2009-2024-fin.csv", sep=";")

print("DATOS DE INICIO")
print(inicio.shape)
print(inicio.columns)

print("\nDATOS DE FIN")
print(fin.shape)
print(fin.columns)