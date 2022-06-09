class Pajaro:

    Alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio. mi color es: {self.color}")

    def volar(self, metros):
        print(f"El pajaro volo {metros} metros")
        self.piar()

    def pintar(self):
        self.color= "Negro"
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")

    @staticmethod
    def mirar():
        print("el pajaro te mira")

rio = Pajaro("amarillo", "canario")

rio.pintar()
rio.volar(50)

Pajaro.poner_huevos(5)

Pajaro.mirar()




