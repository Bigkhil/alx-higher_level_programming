-- list all genres that are not related to dexter
SELECT DISTINCT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.id NOT IN (
	SELECT tv_genres.id
	FROM tv_genres
	JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
	JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_shows.title = 'Dexter'
);
