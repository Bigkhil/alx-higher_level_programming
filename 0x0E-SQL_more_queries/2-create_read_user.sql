-- create database and user
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED by 'user_0d_2_pwd';
GRANT SELECT on `hbtn_0d_2`.* to 'user_0d_2'@'localhost';
flush privileges;
