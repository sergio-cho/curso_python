class animal:

    def __init__(self,edad,color):
        self.edad = edad
        self.color=color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(animal):
    pass

piolin = Pajaro(2,"amarillo")

piolin.nacer()

print(piolin.edad)
