def registro_error(archivo):
    registro = open(archivo , "a")
    registro.write("\nse ha registrado un error de ejecución")
    registro = open(archivo , "r")
    view = print(registro.read())
    registro.close()
    return view


archivo = "prueba1.txt"
registro_error(archivo)