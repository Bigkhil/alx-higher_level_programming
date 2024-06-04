-- create a table with column which has default value equals one
CREATE TABLE IF NOT EXISTS `id_not_null`
(
	`id` INT default 1,
	`name` VARCHAR(256)
);
