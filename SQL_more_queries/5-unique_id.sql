-- Creates table unique_id with id defaulting to 1 and ensures id is unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);