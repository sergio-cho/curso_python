# ABRIMOS EL TEXTO
mi_texto = open("prueba.txt")
#LEEMOS EL ARCHIVO

print(mi_texto.read())

#metodos de strings
linea = mi_texto.readline()

print(linea)

# para archivos pequeños
todas = mi_texto.readlines()

print(todas)
#metodos de listas

todas.pop()
print(todas)

#recomendacion cerrar los archivos
mi_texto.close()