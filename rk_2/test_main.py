import unittest
from main import *

class TestLibraryFunctions(unittest.TestCase):
    def setUp(self):
        self.one_to_many = build_one_to_many(libraries, languages)
        self.many_to_many = build_many_to_many(libraries, languages, libraries_languages)
    
    def test_first_task(self):
        result = first_task(self.one_to_many)
        self.assertIn("Java", result)
        self.assertIn("Javascript", result)
        self.assertEqual(len(result["Java"]), 1)
        self.assertEqual(result["Java"][0], "Guava")
    
    def test_second_task(self):
        result = second_task(self.one_to_many)
        self.assertEqual(result[0][0], "Python")
        self.assertEqual(result[0][1], 16000000)
    
    def test_third_task(self):
        result = third_task(self.many_to_many)
        self.assertEqual(result[0][2], "C/C++")
        self.assertEqual(result[-1][2], "Python")

if __name__ == "__main__":
    unittest.main()