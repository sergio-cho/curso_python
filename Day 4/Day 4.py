# proyecto del dia 4
# '''
#  pediremos el nombre al usuario
#  tratara de adivinar un numero entre el 1 y el 100 con 8 intentos
#     TIENE QUE DECIR SI ES UN VALOR VALIDO
#     TIENE QUE DECIR SI ES UN NUMERO MENOR
#     TIENE QUE DECIR SI ES UN NUMERO MAYOR
#     Y DECIRLE SI ACERTO Y EN CUANTOS INTENTOS
#  '''
from random import *

nombre = input("Ingresa tu nombre ")
numero_secreto = randint(1,101)
print(f"Hola {nombre} estoy pensando en un un numero entre el 1 y el 100")
intentos = 0
while intentos <= 8:
    numero_usuario = int(input("Ingresa el numero que crees que estoy pensando: "))
    if (numero_usuario < 0) and (numero_usuario > 100):
        print("Has ingresado un numero no permitido")
    elif (numero_usuario < numero_secreto):
        print("Escogiste un numero menor al numero secreto")
    elif (numero_usuario > numero_secreto):
        print("Escogiste un numero mayor al numero secreto")
    elif (numero_usuario == numero_secreto):
        print(f"Acertaste al numero secreto en {intentos} , felicidades")
        break
    intentos+=1
if intentos == 8:
    print(f"El numero secreto era {numero_secreto}")
