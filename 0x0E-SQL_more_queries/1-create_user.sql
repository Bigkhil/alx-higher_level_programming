-- create root user
CREATE user if not exists 'user_0d_1'@'localhost' identified by 'user_0d_1_pwd';
GRANT all privileges on *.* to 'user_0d_1'@'localhost';
