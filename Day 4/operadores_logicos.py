'''Operador and'''
from typing import TextIO


mi_bool = 4 < 5 and 5 > 6
# se tiene que cumplir las 2 condiciones para ser verdadero
print(mi_bool)

'''Operador or'''

mi_bool = 4 < 5 or 5 > 6
# se tiene que cumplir 1 de las condiciones para ser verdadero
print(mi_bool)

texto = "esta frase es breve"

mi_bool2 = ("frase" in texto) or ("python" in texto)

print(mi_bool2)

'''Operador not'''

mi_bool = not ("a" == "a")
# se tiene que cumplir la concicion para pasar a lo opuesto 

print(mi_bool)

