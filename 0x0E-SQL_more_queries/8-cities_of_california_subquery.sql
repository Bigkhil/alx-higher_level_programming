-- list all cities of california that are found in hbtn_0d_usa
SELECT c.`id`, c.`name` FROM `cities` AS c, `states` AS s
WHERE s.`name` = 'California' AND
s.`id` = c.`state_id`;
