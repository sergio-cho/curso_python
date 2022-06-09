class animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color=color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal hace un sonido")

class Pajaro(animal):

    def __init__(self,edad,color,altura_vuelo):
        super().__init__(edad , color)
        self.altura_vuelo = altura_vuelo

    # Modifica un metos heredado sobreescribiendolo

    def hablar(self):
        print("Pio")

    def  volar(self,metros):
        print(f"El pajaro volo {metros} metros")


mi_animal = animal(5,"azul")
piolin = Pajaro(2,"amarillo",60)

piolin.hablar()
piolin.volar(50)