import bs4
import requests
import lxml

resultado_titulo = requests.get('https://escueladirecta.com/courses')

sopita = bs4.BeautifulSoup(resultado_titulo.text, 'lxml')

imagenes = sopita.select('.course-box-image')[0]['src']

print(imagenes)

imagen_curso1 = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')

f.write(imagen_curso1.content)

f.close()