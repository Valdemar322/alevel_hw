# FIRST REALIZATION
students = {"Lavrov Voldemar": [10, 10, 11, 12, 12], "Ivanov Ivan": [12, 8, 6, 10, 5],
            "Bebrik Georgiy": [10, 10, 8, 2, 6], "Pekarev Vasiliy": [10, 10, 11, 2, 1],
            "Seleznov Petro": [12, 12, 12, 12, 12], "Sidorov Sidr": [10, 6, 7, 12, 2]}

for k, v in students.items():
    students[k] = sum(v) / len(v)

max_points = max(students.values())
min_points = min(students.values())
worst_student = ""
best_student = ""

for k, v in students.items():
    if min_points == v:
        worst_student = k
    elif max_points == v:
        best_student = k

print(f"Best student: {best_student} has avarage points: {max_points}")
print(f"Worst student: {worst_student} has avarage points: {min_points}")

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# SECOND REALIZATION
students = {"Lavrov Voldemar": [10, 10, 11, 12, 12], "Ivanov Ivan": [12, 8, 6, 10, 5],
            "Bebrik Georgiy": [10, 10, 8, 2, 6], "Pekarev Vasiliy": [10, 10, 11, 2, 1],
            "Seleznov Petro": [12, 12, 12, 12, 12], "Sidorov Sidr": [10, 6, 7, 12, 2]}

for k, v in students.items():
    students[k] = sum(v) / len(v)

max_points = 0
min_points = 0
worst_student = ""
best_student = ""

for k, v in students.items():
    if not max_points:
        max_points = v
        min_points = v
    elif max_points < v:
        max_points = v
        best_student = k
    elif min_points > v:
        min_points = v
        worst_student = k

print(f"Best student: {best_student} has avarage points: {max_points}")
print(f"Worst student: {worst_student} has avarage points: {min_points}")
