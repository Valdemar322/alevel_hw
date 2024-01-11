from datetime import date
import calendar


class Employee:
    def __init__(self, name: str, pay: int):
        self.name = name
        self.pay = pay

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
    def __init__(self, name: str, pay: int, tech_stack: list):
        super().__init__(name, pay)
        self.tech_stack = tech_stack

    def work(self):
        return f"I come to the office and start coding"

    def __add__(self, other: "Developer") -> object:
        if isinstance(other, Developer):
            name = self.name + " " + other.name
            tech_stack = list(set(self.tech_stack + other.tech_stack))
            pay = self.pay if self.pay >= other.pay else other.pay
            return Developer(name, pay, tech_stack)

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


recruiter1 = Recruiter("Alena", 100)
developer1 = Developer("Voldemar", 500, ["Python", "JS", "HTML", "CSS", "SQL"])
developer2 = Developer("Stepa", 300, ["HTML", "CSS"])
print(recruiter1.work())
print(recruiter1)
print(developer1.work())
print(developer1)
print(developer1 > developer2)
print(developer1 >= developer2)
print(developer1 < developer2)
print(developer1 <= developer2)
print(developer1 == developer2)
print(developer1 != developer2)
print(developer1 + developer2)
sum_dev = developer1 + developer2
print(sum_dev.name)
print(sum_dev.tech_stack)
print(sum_dev.pay)
print(developer1.check_salary(8))
