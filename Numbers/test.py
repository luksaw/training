import unittest
import os
from Numbers.Numbers import Numbers


class TestWriteToFile(unittest.TestCase):

    @classmethod
    def tearDown(cls):
        if os.path.exists("output.txt"):
            os.remove("output.txt")

    number = Numbers()

    def test_generate_numbers(self):
        self.assertEqual(len(self.number.generate_numbers(100)), 100)
        self.assertEqual(len(self.number.generate_numbers(-100)), 0)
        self.assertEqual(len(self.number.generate_numbers(0)), 0)
        with self.assertRaises(TypeError):
            self.number.generate_numbers("string")

    def test_write_numbers_to_file(self):
        self.assertFalse(os.path.exists("output.txt"))
        self.number.write_numbers_to_file("output.txt", 100)
        self.assertTrue(os.path.exists("output.txt"))
        with open("output.txt", "r") as f:
            data = f.readlines()
            self.assertEqual(len(data), 100)
            self.assertEqual(int(data[-1].rstrip()), 100)
            self.assertEqual(int(data[0].rstrip()), 1)
            self.assertNotEqual(int(data[-1].rstrip()), 200)

    def test_read_numbers_from_file(self):
        with self.assertRaises(FileNotFoundError):
            self.number.read_numbers_from_file("output.txt")
        self.number.write_numbers_to_file("output.txt", 50)
        data = self.number.read_numbers_from_file("output.txt")
        self.assertEqual(int(data[0]), 1)
        self.assertEqual(int(data[-1]), 50)
        self.assertEqual(int(data[24]), 25)

    def test_print_numbers_from_file(self):
        self.number.write_numbers_to_file("output.txt", 100)
        with self.assertRaises(TypeError):
            self.number.print_numbers_from_file("output.txt", "string")


if __name__ == '__main__':
    unittest.main()
