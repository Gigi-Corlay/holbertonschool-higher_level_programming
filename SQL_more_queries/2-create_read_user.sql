-- Creates the database hbtn_0d_2, the user user_0d_2 with password, grants SELECT on the database, and shows the privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';