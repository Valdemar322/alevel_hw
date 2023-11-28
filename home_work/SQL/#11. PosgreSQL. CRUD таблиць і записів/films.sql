CREATE DATABASE films;

CREATE TABLE actors
(
	actor_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	lastname VARCHAR(100) NOT NULL
);

INSERT INTO actors (name, lastname) VALUES
('Daniel', 'Radcliffe'),
('Jim', 'Carrey'),
('Bruce', 'Lee'),
('George', 'Clooney'),
('Wesley', 'Snipes');

CREATE TABLE films
(
	film_id SERIAL PRIMARY KEY,
	title VARCHAR(100) NOT NULL,
	genre VARCHAR(50) NOT NULL
);

INSERT INTO films (title, genre) VALUES
('The Godfather', 'Thrillers'),
('The Way of the Dragon', 'Thrillers'),
('The Mask', 'Comedy');


CREATE TABLE filmmakers
(
	filmmaker_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	lastname VARCHAR(100) NOT NULL
);

INSERT INTO filmmakers (name, lastname) VALUES
('Quentin', 'Tarantino'),
('David', 'Lynch'),
('Bruce', 'Lee'),
('James', 'Clooney'),
('Wesley', 'Cameron');


SELECT * FROM actors;
SELECT * FROM films;
SELECT * FROM filmmakers;


