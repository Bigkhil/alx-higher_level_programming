-- show some temperatures
SELECT city, AVG(`value`) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY `value` DESC;
