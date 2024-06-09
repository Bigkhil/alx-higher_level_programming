-- list all cities of california that are found in hbtn_0d_usa
SELECT c.`id`, c.`name` FROM `hbtn_0d_usa`.`cities` AS c, `hbtn_0d_usa`.`states` AS s
WHERE s.`name` = 'California' AND
s.`id` = c.`state_id`;
