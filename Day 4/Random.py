from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio = round(uniform(1,50),2)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = [ "azul","verde","morado"]
aleatorio = choice((colores))
print(aleatorio)

numeros = list(range (5,50,5))
shuffle(numeros)
print(numeros)
