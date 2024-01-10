CREATE DATABASE "students-groups-teachers-departments";

CREATE TABLE departments
(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

INSERT INTO departments (name) VALUES
('Computer Science'),
('Mathematics'),
('Physics');



CREATE TABLE teachers
(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	department_id INT NOT NULL REFERENCES departments (id)
);

INSERT INTO teachers (first_name, last_name, department_id) VALUES
('John', 'Doe', 1),
('Jane', 'Smith', 2),
('Robert', 'Johnson', 3),
('Emily', 'Williams', 1),
('Michael', 'Brown', 2);


CREATE TABLE groups
(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	department_id INT NOT NULL REFERENCES departments (id)
);

INSERT INTO groups (name, department_id) VALUES
('CS50', 1),
('Math101', 2),
('Phys101', 3),
('CS101', 1);

CREATE TABLE students
(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	group_id INT NOT NULL REFERENCES groups (id)
);

INSERT INTO students (first_name, last_name, group_id) VALUES
('Alice', 'Johnson', 1),
('Bob', 'Smith', 2),
('Charlie', 'Williams', 3),
('David', 'Brown', 1),
('Eva', 'Davis', 2),
('Frank', 'Miller', 3),
('Grace', 'Jones', 4),
('Henry', 'Anderson', 1),
('Ivy', 'Moore', 2),
('Jack', 'Taylor', 3),
('Kate', 'White', 4),
('Leo', 'Martin', 1),
('Mia', 'Young', 2),
('Noah', 'Lee', 3),
('Olivia', 'Harris', 4),
('Paul', 'Clark', 1),
('Quinn', 'Evans', 2),
('Ryan', 'Wright', 3),
('Sophia', 'Walker', 4),
('Tyler', 'Hill', 1);

SELECT * FROM departments;
SELECT * FROM teachers;
SELECT * FROM groups;
SELECT * FROM students;

-- 1. Вивести ім’я та прізвище студентів разом із назвами їх груп
SELECT students.first_name, students.last_name, groups.name AS group_name
FROM students
JOIN groups ON students.group_id = groups.id;

-- 2. Отримати список викладачів та назви кафедр, на яких вони працюють
SELECT teachers.first_name, teachers.last_name, departments.name AS department_name
FROM teachers
JOIN departments ON teachers.department_id = departments.id;

-- 3. Вивести кількість студентів у кожній групі
SELECT groups.name AS group_name, COUNT(students.group_id) AS count_students
FROM students
JOIN groups ON students.group_id = groups.id
GROUP BY groups.name, students.group_id
ORDER BY count_students;

-- 4. Вивести назву кафедри, імʼя та прізвище викладача, назву групи, імʼя та прізвище студента для викладачів із прізвищем Smith, Williams та Johnson, відсортувати за групою на прізвищем студента. Застосувати JOIN для з’єднання даних з усіх чотирьох таблиць на основі відповідних зовнішніх ключів.
SELECT departments.name AS department, 
teachers.first_name AS teacher_first_name,
teachers.last_name AS teacher_last_name,
groups.name AS group, 
students.first_name AS student_first_name,
students.last_name AS student_last_name
FROM students
JOIN groups ON students.group_id = groups.id
JOIN departments ON groups.department_id = departments.id
JOIN teachers ON teachers.department_id = departments.id
-- WHERE teachers.last_name = 'Smith' OR teachers.last_name = 'Williams' OR teachers.last_name = 'Johnson'
WHERE teachers.last_name IN ('Smith', 'Williams', 'Johnson')
ORDER BY students.last_name;
	
