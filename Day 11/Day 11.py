import bs4
import requests
import lxml

sitio_base = 'https://books.toscrape.com/catalogue/page-{}.html'


# Lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar pagina

for p in range(1, 51):

    # crear sopa de cada pagina
    url = sitio_base.format(p)
    resultado = requests.get(url)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:
        # chequeo pro de estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # guardar titulo en variable
            titulo = libro.select('a')[1]['title']

            titulos_rating_alto.append(titulo)

# Ver los libros depurados
for t in titulos_rating_alto:
    print(t)



