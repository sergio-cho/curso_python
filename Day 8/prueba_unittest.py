import unittest
import cambiatexto

class Probando(unittest.TestCase):
    def test_mayusculas(self):
        word = "hola"
        resultado = cambiatexto.mayusculas(word)
        self.assertEqual(resultado,"HoLA" )

if __name__ == '__main__':
    unittest.main()