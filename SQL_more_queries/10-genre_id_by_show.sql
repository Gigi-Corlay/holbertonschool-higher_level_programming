-- List all TV shows that have at least one genre linked
-- Select the requested columns: tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
-- Start from the tv_shows table
FROM tv_shows
-- Link each tv_show to its genres via tv_show_genres
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Sort by ascending tv_shows.title and tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;