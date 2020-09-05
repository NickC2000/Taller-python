import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(4%2, 0)


if __name__ == '__main__':
    unittest.main()
