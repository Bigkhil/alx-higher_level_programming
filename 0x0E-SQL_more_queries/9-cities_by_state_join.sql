-- list all cities in the database
SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
FROM `cities`, `states`
WHERE `cities`.`state_id` = `states`.`id`
GROUP BY `cities`.`name`
ORDER BY `cities`.`id`;
