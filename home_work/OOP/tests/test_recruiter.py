from unittest import TestCase
from _17.oop_employee import Recruiter, Employee
import os


class TestRecruiter(TestCase):
    def test_clean(self):
        if os.path.exists("emails.csv"):
            os.remove("emails.csv")

    def test_recruiter_positive(self):
        recruiter1 = Recruiter("Alena", 100, "Ahrysha@gugla.com")
        self.assertTrue(isinstance(recruiter1, Employee))
        self.assertTrue(isinstance(recruiter1.name, str))
        self.assertTrue(isinstance(recruiter1.pay, int))
        self.assertTrue(isinstance(recruiter1.email, str))
        self.assertEqual(recruiter1.work(), f"I come to the office and start to hiring")
        self.assertEqual(str(recruiter1), f"Recruiter: {recruiter1.name}")

    def test_recruiter_negative(self):
        recruiter1 = Recruiter("Alena", 100, "Ahrysha@guglas.com")
        self.assertFalse(isinstance(recruiter1.name, int))
        self.assertFalse(isinstance(recruiter1.pay, str))
        self.assertFalse(isinstance(recruiter1.email, int))
        self.assertNotEqual(recruiter1.work(), f"")
        self.assertNotEqual(str(recruiter1), f"Recruiter: {recruiter1.pay}")
