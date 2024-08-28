import unittest
from upper_name import convert_to_uppercase

class TestUpperName(unittest.TestCase):
    def test_convert_to_uppercase(self):
        self.assertEqual(convert_to_uppercase("John Doe"), "JOHN DOE")
        self.assertEqual(convert_to_uppercase("hello world"), "HELLO WORLD")
        self.assertEqual(convert_to_uppercase("Python"), "PYTHON")
        self.assertEqual(convert_to_uppercase(""), "")

if __name__ == "__main__":
    unittest.main()
