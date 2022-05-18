nombre= input("Ingresa tu nombre: ")
ventas=int(input("Ingresa tus ventas del mes: "))
ganancias= ventas * .13
print(f"Ok{nombre}.Este mes ganaste ${round(ganancias,2)}")