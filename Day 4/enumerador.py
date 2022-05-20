lista = ["a","b","c"]
indice = 0

for item in enumerate(lista):
    print(item)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i , nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(i)