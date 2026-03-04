-- Select the requested columns.
SELECT cities.id, cities.name, states.name
-- Start with the cities table.
FROM cities
-- link each city to its state.
JOIN states ON cities.state_id = states.id
-- sort by ascending cities.id.
ORDER BY cities.id ASC;