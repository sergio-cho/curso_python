from pathlib import Path

carpeta = Path("/home/sergio/Documentos/curso_python/Alternativos")

archivo = carpeta / "otro_archivo.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())