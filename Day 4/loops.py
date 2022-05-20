'''Bucle for'''
from operator import le


lista = ["a","b","c"]

for letra in lista:
    #poemos obteneer el indice 
    numero_letra = lista.index(letra)+1
    #poemos imprimir su valor y su indice 
    print(f"Soy la letra {numero_letra}: {letra} ")

print("ejemplo 2")
lista_nombres = ["sergio","abigail","omar","luis"]    

for nombre in lista_nombres:
    if nombre.startswith("l"):
        print(nombre)

print("ejemplo 3")

numeros = [1,2,3,4,5]
mi_valor=0
for numero in numeros:
    mi_valor= mi_valor+numero
    print(mi_valor)


'''Bucle while'''
monedas = 5 

while monedas >0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1

respuesta = 's'
# funcion de pass 
while respuesta == 's':
     pass
print("hola")

# funcion de break
nombre = input("Tu nombre")

for letra in nombre:
    if letra == 'r':
        break
        con
    print(letra)