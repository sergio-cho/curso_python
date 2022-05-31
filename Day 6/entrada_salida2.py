# ABRIMOS EL TEXTO Y SI NO EXISTE PYTHON LO CREA POR DEFECTO

# ABRIMOS EL TEXTO
mi_texto = open("prueba1.txt", "w")
# sOLO UN STRING
mi_texto.write("holi")
mi_texto = open("prueba1.txt", "r")
si = mi_texto.read()
print(si)
#ESCRIBE VARIOS STRINGS EN UNA SOLA LINEA

# mi_texto.writelines(["Hola ", "que ", "pasa ","chavales"])

mi_texto.close()