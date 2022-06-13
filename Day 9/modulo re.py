import  re
texto = "lorem ipsum dolor sit amet, lorem  consectetur adipisicing elit. Nam vero lorem "

patron = 'lorem'

busqueda = re.findall(patron, texto)

print(busqueda)

for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())