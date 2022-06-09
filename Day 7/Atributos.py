class Pajaro:
    #Atributos de clase

    Alas = True

    # Atributos de instancia ya que cualquier objeto puede tenerlo distinto

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie



mi_pajaro = Pajaro("Azul" , "Loro")

print(mi_pajaro.especie)

print(Pajaro.Alas)

print(mi_pajaro.Alas)

