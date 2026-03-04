-- 0-privileges.sql
-- Displays all privileges granted to user_0d_1 and user_0d_2

-- Step 1: Make sure the users exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Step 2: Grant privileges (can be adjusted)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

-- Step 3: Show privileges for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';