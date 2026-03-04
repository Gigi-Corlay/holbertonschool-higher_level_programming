-- Creates table force_name with id as primary key and name that cannot be null
CREATE TABLE IF NOT EXISTS force_name (
    id INT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
