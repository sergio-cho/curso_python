def decorar(funcion):

    def otra(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra

def mayuscula(texto):
    print(texto.upper())
@decorar
def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar(mayuscula)

mayuscula_decorada("sergio")

