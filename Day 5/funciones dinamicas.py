def chequear (lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass

resultado = chequear([55,99,6000,777])
print(resultado)

lista_numeros=[1,50,500,5000,750]

def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if n in range(0,1000):
            suma = suma + n
        else:
            pass
    return suma



