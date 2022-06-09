class padre:

    def hablar(self):
        print("hola")

class madre:
    def reir(self):
        print("jajaja")

    def hablar(self):
        print("que tal")

# si hay metodos con nombres iguales va a utilizar el que se encuentre primero

class hijo(padre , madre):
    pass

class nieto(hijo):
    pass

mi_nieto = nieto()

mi_nieto.hablar()

mi_nieto.reir()