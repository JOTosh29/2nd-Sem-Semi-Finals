-- Create the database
CREATE DATABASE IF NOT EXISTS mydatabase;

-- Use the created database
USE mydatabase;

-- Create the table
CREATE TABLE IF NOT EXISTS mytable (
    student_code INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    age INT NOT NULL,
    course VARCHAR(255),
    year INT
);

-- Insert a record into the table
INSERT INTO mytable (last_name, first_name, middle_name, age, course, year)
VALUES ('Doe', 'John', 'William', 25, 'Computer Science', 2023);

-- Update a record in the table
UPDATE mytable
SET age = 26
WHERE student_code = 1;

-- Delete a record from the table
DELETE FROM mytable
WHERE student_code = 1;

-- Search for records in the table
SELECT * FROM mytable;
