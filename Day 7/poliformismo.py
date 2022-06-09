class Vaca:
    def __init__(self , nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " muuuu")

class Oveja:
    def __init__(self ,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " beeeee")

vaca1 = Vaca("si")
obeja1 = Oveja("Si")

animales = [vaca1 ,obeja1]

for i in animales:
    i.hablar()

def animal_habla(animal):
    print("esto es una funcion")
    animal.hablar()

animal_habla(vaca1)