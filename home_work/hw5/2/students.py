students = {"Ivanov Ivan": ("Python",),
            "Gladkova Anastasiya": ("Python", "FrontEnd"),
            "Sidorov Gennadiy": ("Java",),
            "Bober Illya": ("Python", "FullStack"),
            "Voloshin Ivan": ("Python",),
            "Zaharova Anna": ("Python", "FrontEnd", "FullStack", "Java"),
            "Robinovich Izya": ("Python",),
            "Barabashkin Arsen": ("FrontEnd",),
            "Kutuzov Stepan": ("FrontEnd", "Java"),
            "Burunduk Alyona": ("Python", "FrontEnd")}

students_more2_groups = []
students_nofrontend_group = []
students_python_java = []
python = "Python"
java = "Java"

for k, v in students.items():
    if len(v) > 1:
        students_more2_groups.append(k)
    if not ("FrontEnd" in v or "FullStack" in v):
        students_nofrontend_group.append(k)
    if (python in v) or (java in v):
        students_python_java.append(k)

print(f"Students who study in two or more groups: {students_more2_groups}")
print(f"Students who don't study on the front-end: {students_nofrontend_group}")
print(f"Students learning Python or Java: {students_python_java}")
