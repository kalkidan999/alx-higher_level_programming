--  script that lists all cities contained in the database hbtn_0d_usa
-- display ONLY: cities.id - cities.name - states.name,Results must be sorted in asc order by cities.id
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.id = states.id ORDER BY cities.id ASC
