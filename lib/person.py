class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal",
        "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"
    ]
    
    def __init__(self, name="Unknown", job="Unknown"):
        self._name = None
        self._job = None
        self.name = name 
        self.job = job 

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

import io
import sys
import unittest

class TestPerson(unittest.TestCase):
    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        guido = Person(name="Guido", job="ITC")
        self.assertEqual(guido.name, "Guido")

    def test_valid_name_title_case(self):
        '''converts name to title case and saves if between 1 and 25 characters'''
        guido = Person(name="guido van rossum", job="ITC")
        self.assertEqual(guido.name, "Guido Van Rossum")

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="Guido", job="Benevolent dictator for life")
        sys.stdout = sys.__stdout__
        self.assertIn("Job must be in list of approved jobs.", captured_out.getvalue())

    def test_job_in_list(self):
        '''saves job if in job list.'''
        guido = Person(name="Guido", job="ITC")
        self.assertEqual(guido.job, "ITC")

if __name__ == '__main__':
    unittest.main()
