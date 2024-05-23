import unittest
import io
import sys
from dog import Dog

class TestDog(unittest.TestCase):
    def setUp(self):
        self.captured_out = io.StringIO()
        self.captured_err = io.StringIO()
        sys.stdout = self.captured_out
        sys.stderr = self.captured_err

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        Dog(name=123, breed="Beagle") 
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        self.assertIn("Name must be string between 1 and 25 characters.", self.captured_err.getvalue().strip())

    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        Dog(name="", breed="Beagle")
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        self.assertIn("Name must be string between 1 and 25 characters.", self.captured_err.getvalue().strip())

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        Dog(name="What do dogs do on their day off? Can't lie around - that's their job.", breed="Beagle")
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        self.assertIn("Name must be string between 1 and 25 characters.", self.captured_err.getvalue().strip())

    def test_breed_not_in_list(self):
        '''prints "Breed must be in list of approved breeds." if not in breed list.'''
        Dog(name="Fido", breed="Human")
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        self.assertIn("Breed must be in list of approved breeds.", self.captured_err.getvalue().strip())

    def test_breed_in_list(self):
        '''saves breed if in breed list.'''
        fido = Dog(name="Fido", breed="Pug")
        self.assertEqual(fido.breed, "Pug")

if __name__ == '__main__':
    unittest.main()
