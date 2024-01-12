from unittest import TestCase
from _17.oop_employee import Developer, Employee
import os


class TestDeveloper(TestCase):
    def test_clean(self):
        if os.path.exists("emails.csv"):
            os.remove("emails.csv")

    def test_developer_positive(self):
        developer1 = Developer("Voldemar", 500, "test-dev@gugla.com", ["Python", "JS", "HTML", "CSS", "SQL"])
        developer2 = Developer("Stepa", 300, "pretykity-dev@gugel.com", ["HTML", "CSS"])
        developer3 = developer1 + developer2
        self.assertTrue(isinstance(developer1, Employee))
        self.assertTrue(developer1 > developer2)
        self.assertTrue(developer1 >= developer2)
        self.assertTrue(developer1 != developer2)
        self.assertTrue(isinstance(developer3, Developer))
        self.assertEqual(developer3.pay, developer1.pay)
        self.assertEqual(developer3.name, f"{developer1.name} {developer2.name}")
        self.assertEqual(str(developer1), f"Developer: {developer1.name}")
        self.assertTrue(isinstance(developer1.name, str))
        self.assertTrue(isinstance(developer1.pay, int))
        self.assertTrue(isinstance(developer1.email, str))
        self.assertTrue(isinstance(developer1.tech_stack, list))

    def test_developer_negative(self):
        developer1 = Developer("Voldemar", 500, "test-dev@guglas.com", ["Python", "JS", "HTML", "CSS", "SQL"])
        developer2 = Developer("Stepa", 300, "pretykity-dev@gugels.com", ["HTML", "CSS"])
        developer3 = developer1 + developer2
        self.assertFalse(developer1 < developer2)
        self.assertFalse(developer1 <= developer2)
        self.assertFalse(developer1 == developer2)
        self.assertFalse(isinstance(developer3, str))
        self.assertNotEqual(developer3.pay, developer2.pay)
        self.assertNotEqual(developer3.name, f"{developer1.name}{developer2.name}")
        self.assertNotEqual(str(developer1), f"{developer1.name}")
        self.assertFalse(isinstance(developer1.name, int))
        self.assertFalse(isinstance(developer1.pay, str))
        self.assertFalse(isinstance(developer1.email, list))
        self.assertFalse(isinstance(developer1.tech_stack, str))
