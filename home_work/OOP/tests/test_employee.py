from unittest import TestCase
from _17.oop_employee import Employee, EmailAlreadyExistsException
import os


class TestEmployee(TestCase):
    def test_clean(self):
        if os.path.exists("emails.csv"):
            os.remove("emails.csv")

    def test_employee_positive(self):
        employee1 = Employee("Voldemar", 500, "test@gugla.com")
        employee2 = Employee("Stepa", 300, "pretykity@gugel.com")
        self.assertTrue(isinstance(employee1.name, str))
        self.assertTrue(isinstance(employee1.pay, int))
        self.assertTrue(isinstance(employee1.email, str))
        self.assertTrue(isinstance(employee1.check_salary(10), int))
        self.assertTrue(os.path.exists("emails.csv"))
        with self.assertRaises(EmailAlreadyExistsException):
            employee1.validate_email(f"{employee1.email}")
        self.assertTrue(employee1 > employee2)
        self.assertTrue(employee1 >= employee2)
        self.assertTrue(employee1 != employee2)
        self.assertEqual(employee1.work(), f"I come to the office.")

    def test_employee_negative(self):
        employee1 = Employee("Voldemar", 500, "test@guglas.com")
        employee2 = Employee("Stepa", 300, "pretykity@gugels.com")
        self.assertFalse(isinstance(employee1.name, int))
        self.assertFalse(isinstance(employee1.pay, str))
        self.assertFalse(isinstance(employee1.email, int))
        self.assertNotEqual(employee1.check_salary(10), 0)
        self.assertFalse(os.path.exists("emails.csvs"))
        self.assertFalse(employee1 < employee2)
        self.assertFalse(employee1 <= employee2)
        self.assertFalse(employee1 == employee2)
        self.assertNotEqual(employee1.work(), f"")
