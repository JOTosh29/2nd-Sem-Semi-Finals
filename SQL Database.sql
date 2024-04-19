-- Create the database
CREATE DATABASE IF NOT EXISTS mydatabase;

-- Use the created database
USE mydatabase;

-- Create the table
CREATE TABLE IF NOT EXISTS admitted_students (
    student_code INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    age INT NOT NULL,
    course VARCHAR(255),
    year INT
);

-- Create table for transfer students
CREATE TABLE IF NOT EXISTS transfer_students (
    student_code INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    age INT NOT NULL,
    course VARCHAR(255),
    year INT
);

-- Create table for shifters
CREATE TABLE IF NOT EXISTS shifters (
    student_code INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    age INT NOT NULL,
    course VARCHAR(255),
    year INT
);


-- Insert a record into the table
INSERT INTO admitted_students (last_name, first_name, middle_name, age, course, year)
VALUES ('Bognalbal', 'Jim Owen','Katigbak', 25, 'BSCS', 2024);

-- Insert records into transfer_students table
INSERT INTO transfer_students (last_name, first_name, middle_name, age, course, year)
VALUES ('Doe', 'John', 'Michael', 22, 'Biology', 2023),
       ('Smith', 'Jane', 'Elizabeth', 20, 'Physics', 2022);

-- Insert records into shifters table
INSERT INTO shifters (last_name, first_name, middle_name, age, course, year)
VALUES ('Garcia', 'Maria', 'Santos', 21, 'Chemistry', 2023),
       ('Nguyen', 'David', 'Minh', 23, 'Mathematics', 2022);


-- Update a record in the table
UPDATE admitted_students
SET student_code = 1
WHERE student_code = 8;

-- Delete a record from the table
DELETE FROM admitted_students
WHERE student_code = 7;

-- Search for records in the table
SELECT * FROM admitted_students;

-- Search for records in transfer_students table
SELECT * FROM transfer_students;

-- Search for records in shifters table
SELECT * FROM shifters;

