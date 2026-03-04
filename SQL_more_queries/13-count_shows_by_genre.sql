-- List all TV genres that have at least one show linked
-- Display two columns: genre - number_of_shows
SELECT tv_genres.name AS genre, 
       COUNT(tv_show_genres.show_id) AS number_of_shows
-- Start from the tv_genres table
FROM tv_genres
-- Join with tv_show_genres to count linked shows
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Group by genre name to count shows per genre
GROUP BY tv_genres.name
-- Sort by descending number of shows
ORDER BY number_of_shows DESC;