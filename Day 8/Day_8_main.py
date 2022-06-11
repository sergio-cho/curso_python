import Day_8
def menu():
    print("Bienvenido a farmacia guadalajara")
    while True:
        print(f'''
        Que departamento visita?
        [1]-Perfumeria
        [2]-Farmacia
        [3]-Cosmeticos
        ''')
        try:
            rubro = int(input())
            [1,2,3].index(rubro)
        except:
            print("No has escogido un valor valido")
        else:
            break

    Day_8.decorar(rubro)

def inicio():
    while True:
        menu()
        try:
            otro = input("Quieres sacar otro turno S/N").upper()
        except:
            print("No has escogido un valor valido")
        else:
            if otro == "N":
                print("Bye")
                break

inicio()