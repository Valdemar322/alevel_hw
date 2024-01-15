import csv
from _20.oop_hw_20 import logger


class Candidate:
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 email: str,
                 tech_stack: tuple,
                 main_skill: str,
                 main_skill_grade: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    @logger
    def generate_candidates(cls, file_path: str) -> list:
        candidates = []
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for line in csv_reader:
                try:
                    full_name, email, tech_stack, main_skill, main_skill_grade = line
                    full_name = full_name.split(" ")
                    first_name, last_name = full_name
                except ValueError as e:
                    with open("logs.txt", "a") as file:
                        file.write(str(e))
                else:
                    candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
                    candidates.append(candidate)
        return candidates


if __name__ == "__main__":
    candidates = Candidate.generate_candidates("candidates.csv")
    for obj in candidates:
        print(obj.first_name, obj.last_name, obj.email, obj.tech_stack, obj.main_skill, obj.main_skill_grade)
