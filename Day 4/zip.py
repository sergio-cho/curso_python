''' Junta 2 listas en una sola tupla '''
nombres = ["sergio","nayvi","ivan"]
edades = [19 , 20 , 19]
paises = ["lima","mexico","madrid"]
combinados = list(zip(nombres , edades ,paises))

print(combinados)

for nombre , edad , pais in combinados:
    print(f"{nombre} tiene {edad} años y vive en {pais}")

