import math
import os , re , time
from pathlib import Path
from datetime import date
# Fecha
inicio = time.time()
fecha =date.today().strftime("%d/%m/%y")

# funcion para recore los directorios
ruta = "/home/sergio/Documentos/curso_python/Day 9/Mi_Gran_Directorio"
print(ruta)
patron = r'N\D{3}-\d{5}'
num_encontrado = []
archivos_encontrados = []

def buscar(archivo,patron):

    este_archivo = open(archivo,'r')
    texto = este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ''

def listas():
    for capeta,subcarpetas,archivos in os.walk(ruta):
        for a in archivos:
            resultado = buscar(Path(capeta,a),patron)
            if resultado != '':
                num_encontrado.append(resultado.group())
                archivos_encontrados.append(a.title())
def resultado():
    indice= 0
    print("-" * 30)
    print(f"Fecha de busqueda {fecha}\n")
    print("Archivo\t\t\tNro.Serie")
    print("-"*25)
    for a in archivos_encontrados:
        print(f"{a}\t{num_encontrado[indice]}")
        indice += 1
    print(f"\nNumeros encontrados: {len(num_encontrado)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duracion de la busqueda: {math.ceil(duracion)}")
    print("-" * 30)


listas()
resultado()