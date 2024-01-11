from datetime import date
import calendar
import csv
import datetime


class EmailAlreadyExistsException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.exception_handling()

    def exception_handling(self):
        with open("logs.txt", "a") as file:
            file.write(f"Date: {str(datetime.datetime.now())[:-7]} | {self.message} \n")


class Employee:
    def __init__(self, name: str, pay: int, email: str):
        self.name = name
        self.pay = pay
        self.email = email
        self.save_email()

    def work(self) -> str:
        return f"I come to the office."

    """Simple level"""
    # def check_salary(self, days: int) -> int:
    #     return self.pay * days

    """Hard level"""

    def check_salary(self, days: int) -> int:
        salary = 0
        today = date.today()
        for day in range(1, days + 1):
            current_week_day = calendar.weekday(today.year, today.month, day)
            if current_week_day < 5:
                salary += self.pay
        return salary

    def save_email(self):
        with open("emails.csv", "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([self.email])

    def validate_email(self, email: str):
        with open("emails.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if email in line:
                    raise EmailAlreadyExistsException("EmailAlreadyExistsException!")

    def __lt__(self, other):
        return self.pay < other.pay

    def __gt__(self, other):
        return self.pay > other.pay

    def __le__(self, other):
        return self.pay <= other.pay

    def __ge__(self, other):
        return self.pay >= other.pay

    def __eq__(self, other):
        return self.pay == other.pay

    def __ne__(self, other):
        return self.pay != other.pay


class Recruiter(Employee):
    def work(self):
        return f"I come to the office and start to hiring"

    def __str__(self):
        return f"Recruiter: {self.name}"


class Developer(Employee):
    def __init__(self, name: str, pay: int, email: str, tech_stack: list):
        super().__init__(name, pay, email)
        self.tech_stack = tech_stack

    def work(self):
        return f"I come to the office and start coding"

    def __add__(self, other: "Developer") -> object:
        if isinstance(other, Developer):
            dev = Developer(self.name, self.pay, self.email, self.tech_stack)
            dev.name = self.name + " " + other.name
            if len(self.tech_stack) >= len(other.tech_stack):
                dev.tech_stack = set(self.tech_stack) - set(other.tech_stack)
            else:
                dev.tech_stack = set(other.tech_stack) - set(self.tech_stack)
            dev.pay = self.pay if self.pay >= other.pay else other.pay
            return dev

    def __str__(self):
        return f"Developer: {self.name}"

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)


# recruiter1 = Recruiter("Alena", 100, "Ahrysha@gugla.com")
# developer1 = Developer("Voldemar", 500, "test@gugla.com", ["Python", "JS", "HTML", "CSS", "SQL"])
# developer2 = Developer("Stepa", 300, "pretykity@gugel.com", ["HTML", "CSS"])

# recruiter1.validate_email("Ahrysha@guglaaa.com")
# developer1.validate_email("test@guglaasas.com")
# developer2.validate_email("pretykity@gugel.com")

# print(recruiter1.work())
# print(recruiter1)
# print(developer1.work())
# print(developer1)
# print(developer1 > developer2)
# print(developer1 >= developer2)
# print(developer1 < developer2)
# print(developer1 <= developer2)
# print(developer1 == developer2)
# print(developer1 != developer2)
# print(developer1 + developer2)
# sum_dev = developer1 + developer2
# print(sum_dev.name)
# print(sum_dev.tech_stack)
# print(sum_dev.pay)
# print(developer1.check_salary(8))
