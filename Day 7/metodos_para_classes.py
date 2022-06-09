class Pajaro:

    Alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro volo {metros} metros")


rio = Pajaro("amarillo", "canario")
