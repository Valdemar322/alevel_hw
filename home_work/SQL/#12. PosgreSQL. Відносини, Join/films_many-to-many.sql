-- 2. Переписати базу даних фільмів (із таблицями акторів, фільмів, режисерів), додавши many-to-many звʼязки

-- Rename id column
ALTER TABLE actors
RENAME COLUMN actor_id TO id;

-- Rename id column
ALTER TABLE films
RENAME COLUMN film_id TO id;

-- Rename id column
ALTER TABLE filmmakers
RENAME COLUMN filmmaker_id TO id;

-- Correct column value from 'jim' to 'Jim'
UPDATE actors
SET name = 'Jim' 
WHERE id = 2;

-- CREATE third table with connection (films - actors)
CREATE TABLE films_actors
(
  id SERIAL PRIMARY KEY,
  film_id INT NOT NULL REFERENCES films (id),
  actor_id INT NOT NULL REFERENCES actors (id)
);

-- Filling table (many-to-many)
INSERT INTO films_actors (film_id, actor_id) VALUES
(3, 2),
(2, 3);


-- CREATE third table with connection (films - filmmakers)
CREATE TABLE films_filmmakers
(
  id SERIAL PRIMARY KEY,
  film_id INT NOT NULL REFERENCES films (id),
  filmmaker_id INT NOT NULL REFERENCES filmmakers (id)
);

-- DELETE FROM films_filmmakers
-- WHERE id = 1;

-- Filling table (many-to-many)
INSERT INTO films_filmmakers (film_id, filmmaker_id) VALUES
(2, 3);


-- SELECT * FROM actors;
-- SELECT * FROM films;
-- SELECT * FROM filmmakers;
-- SELECT * FROM films_actors;
-- SELECT * FROM films_filmmakers;


SELECT actors.name, actors.lastname, films.title
FROM actors
JOIN films_actors ON films_actors.actor_id = actors.id
JOIN films ON films_actors.film_id = films.id;


SELECT films.title, filmmakers.name, filmmakers.lastname
FROM films
JOIN films_filmmakers ON films_filmmakers.film_id = films.id
JOIN filmmakers ON films_filmmakers.filmmaker_id = filmmakers.id;

