-- Creates user_0d_1 if it does not exist, grants all privileges, and displays the user's privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
