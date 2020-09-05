import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        edadActual = 20
        añoActual = 2020
        edadFinal = edadActual + (2070 - añoActual)

        self.assertEqual(edadFinal, 70)

if __name__ == '__main__':
    unittest.main()
