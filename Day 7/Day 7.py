class Persona:
    def __init__(self,nombre , apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,num_cuenta,saldo):
        super().__init__(nombre,apellido)
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def __str__(self):
        return print(f"Tu nombre es {self.nombre} {self.apellido} tu numero de cuenta es  {self.num_cuenta} y tu saldo es: {self.saldo}")

    def depositar(self,dinero_por_agregar):
        self.saldo = self.saldo + dinero_por_agregar
        print(f"Se agrego con exito , tu nuevo saldo es: {self.saldo}")

    def retirar(self,dinero_por_retirar):
        if self.saldo >= dinero_por_retirar:
            self.saldo -= dinero_por_retirar
            print(f"Se agrego con exito , tu nuevo saldo es: {self.saldo}")
        else:
            print("Fondos insuficientes")


def crear_persona():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    numero_cuenta = input("Ingresa tu numero de cuenta: ")
    saldo = 0
    cliente = Cliente(nombre , apellido, numero_cuenta , saldo)
    return cliente

def menu():
    cliente = crear_persona()
    x = False
    cliente.__str__()
    while x is not True:
        print(f'''Bienvenido {cliente.nombre}
                [1]-Depositar
                [2]-Retirar
                [3]-Salir
                ''')
        opcion = int(input("Que operacion quieres realizar?"))
        if opcion not in range(1,4):
            print("Intentalo de nuevo")
            pass
        elif opcion == 1:
            deposito = int(input("Cuanto dinero deseas agregar: "))
            cliente.depositar(deposito)
        elif opcion == 2:
            retiro= int(input("Cuanto dinero desea retirar: "))
            cliente.retirar(retiro)
        elif opcion == 3:
            x= True

menu()