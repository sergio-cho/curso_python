# Pedimos un texto al usuario
texto= input("""Ingresa un texto: """)
#lo pasamos tomo a minusculas
texto = texto.lower()
# lo dividimos para hacerlo lista
new_text= texto.split()
# Pedimos 3 letras
letra_1 = input("Ingresa una letra: ").lower()
letra_2 = input("Ingresa una letra: ").lower()
letra_3 = input("Ingresa una letra: ").lower()

#Agregamos las letras a una lista

my_letters =[letra_1,letra_2,letra_3]

# contamos los valores

conteo_1 = texto.count(letra_1)
conteo_2 = texto.count(letra_2)
conteo_3 = texto.count(letra_3)
#resultados

print(f"La letra {letra_1} se repite: {conteo_1}")
print(f"La letra {letra_2} se repite: {conteo_2}")
print(f"La letra {letra_3} se repite: {conteo_3}")

# primer y ultimo caracter
first = texto[0]
last = texto[-1]
print(f"la primera letra es {first} y la ultima letra es: {last}")

#python in lista
find_python = "python" in texto
dic = {True:"si",False:"no"}

print(f"En texto aparece python {dic[find_python]}")
#palabras en orden inverso
new_text.reverse()
text_inver= " ".join(new_text)

print(f"El orden invertido del texto es el sig: {text_inver}")

#palabras en el texto
print(f"Las palabras en el texto son: {len(new_text)}")


