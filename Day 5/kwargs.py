def suma(**kwargs):
    print(type(kwargs))
    total= 0
    for clave , valor in kwargs.items():
        print(f"{clave} = {valor}" )
        total += valor
    return total

print(suma(x=3 , y= 5 , z = 2))

def prueba(num1,num2 , *args , **kwargs):
    print({num1})
    print({num2})

    for arg in args:
        print(f"arg = {arg}")

    for clave , valor in kwargs.items():
        print(f"{clave} = {valor}" )

print(prueba(5,7,77,66,99,y=5, x=9))


def describir_persona(nombre, **kwargs):
    print(f"Caracteristicas de {nombre}")
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")

describir_persona("Maria", color_ojos="azules", color_pelo="rubio")