-- create database and user
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE user if not exists 'user_0d_2'@'localhost' identified by 'user_0d_2_pwd';
GRANT select on hbtn_0d_2.* to 'user_0d_2'@'localhost';
