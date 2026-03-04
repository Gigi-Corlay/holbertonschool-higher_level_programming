-- List all TV shows including those without a genre
-- Select the requested columns: tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
-- Start from the tv_shows table
FROM tv_shows
-- Use LEFT JOIN to include shows that may not have a genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Sort by ascending tv_shows.title and tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;