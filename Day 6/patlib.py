from pathlib import Path

carpeta = Path("/home/sergio/Documentos/curso_python/Day 6/prueba2.txt")

if not carpeta.exists():
    print("El archivo no existe")
else:
    print("Ese archivo ya existe")