class Employee:
    def __init__(self, name: str, pay: int):
        self.name = name
        self.pay = pay

    def work(self) -> str:
        return f"I come to the office."


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
    def work(self):
        return f"I come to the office and start coding"

    def __str__(self):
        return f"Developer: {self.name}"


recruiter1 = Recruiter("Alena", 100)
developer1 = Developer("Voldemar", 500)

print(recruiter1.work())
print(recruiter1)
print(developer1.work())
print(developer1)
print(developer1 > recruiter1)
print(developer1 >= recruiter1)
print(developer1 < recruiter1)
print(developer1 <= recruiter1)
print(developer1 == recruiter1)
print(developer1 != recruiter1)
