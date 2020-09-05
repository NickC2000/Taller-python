import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        palabra = 'Hola'
        caracterUno = palabra[0]
        caracterDos = palabra[len(palabra)-1]

        self.assertEqual('H', caracterUno)
        self.assertEqual('a', caracterDos)


if __name__ == '__main__':
    unittest.main()
