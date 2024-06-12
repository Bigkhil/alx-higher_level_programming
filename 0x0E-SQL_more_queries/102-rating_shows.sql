-- list all shows by their ratings
SELECT tv_shows.title AS title, sum(tv_show_ratings.rate) AS rating
FROM tv_show_ratings
JOIN tv_shows ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
