
def Perfumeria():
    turno = 20
    while True:
        turno +=1
        yield f"P-{turno}"

def Farmacia():
    turno = 20
    while True:
        turno +=1
        yield f"F-{turno}"

def Cosmeticos():
    turno = 20
    while True:
        turno +=1
        yield f"C-{turno}"

p = Perfumeria()
f = Farmacia()
c = Cosmeticos()

def decorar(rubro):
    print("Su turno es:")
    if rubro == 1:
        print(next(p))
    elif rubro == 2:
        print(next(f))
    else:
        print(next(c))
    print("Pronto sera atendido")



