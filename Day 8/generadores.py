def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista

def mi_generador():
    for x in range(1, 5):
        yield x * 10

g = mi_generador()
print(mi_funcion())

print(g)
