from random import *
'''
# Lista ninicial
palitos = ["-","--","---","----"]
# Mezclar los palitos

def mezclar (lista):
    shuffle(lista)
    return lista

# PEDIR EL INTENTO
def suerte():
    intento = ""

    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

# COMPROBACION
def chequeo(lista,intento):
    if lista[intento-1] == "-":
        print("Te toco lavar los platos")
    else:
        print("Te salvaste")
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = suerte()
chequeo(palitos_mezclados,seleccion)
'''
from random import *

# datos
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    return (dado1, dado2)

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
       return f"La suma de tus dados es {suma_dados}.Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}.Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece la jugada ganadora"

dado1,dado2 = lanzar_dados()
evaluar_jugada(dado1, dado2)

lista_numeros = [1, 2, 15, 7, 2,8]

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista

def promedio(lista):
    acum = 0
    for n in lista:
        acum = n + acum
    promedio = acum / len(lista)
    return f"El promedio es {promedio}"

n_list = reducir_lista(lista_numeros)

print(promedio(n_list))


