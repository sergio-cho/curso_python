from collections import Counter , defaultdict
numeros = [1,2,3,4,5,5,8,4,9,2,3,5,1,6]

print(Counter(numeros))

mi_dic = defaultdict(lambda : "nada")

mi_dic["uno"] = "verde"

print(mi_dic["dos"])

from collections import deque
lista_ciudades=deque()
lista_ciudades.appendleft(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)