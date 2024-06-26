-- list number of shows linked to each genre
SELECT tv_genres.name AS genre, count(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
