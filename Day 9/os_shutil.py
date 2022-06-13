import os
import shutil
print(os.getcwd())
os.chdir("/home/sergio/Documentos/curso_python/Day 9/Mi_Gran_Directorio")
print(os.system("ls -la "))
print(os.getcwd())
archivo = open("curso.txt","w")

archivo.write("hola estoy en el curso")

archivo.close()

# Mover archivo
#shutil.move("curso.txt","/home/sergio/Documentos/curso_python/Alternativos")

