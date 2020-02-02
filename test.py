import unittest
from Numbers.Numbers import Numbers


class TestWriteToFile(unittest.TestCase):

    number = Numbers()

    def test_generate_numbers(self):
        self.assertEqual(len(self.number.generate_numbers(100)), 100)
        self.assertEqual(len(self.number.generate_numbers(-100)), 0)
        self.assertEqual(len(self.number.generate_numbers(0)), 0)
        with self.assertRaises(TypeError):
            self.number.generate_numbers("string")

    def test_print_numbers(self):
        pass


if __name__ == '__main__':
    unittest.main()
