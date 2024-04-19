	-- create a databasea
	CREATE DATABASE mydatabase;

	-- use the created database
	USE mydatabase;

	-- create a table
	CREATE TABLE mytable (
		student_code INT PRIMARY KEY AUTO_INCREMENT,
		last_name VARCHAR(255) NOT NULL,
		first_name VARCHAR(255) NOT NULL,
		middle_name VARCHAR(255),
		age INT NOT NULL,
		course VARCHAR(255),
		year INT
	);

	-- delete the created table
	DROP TABLE mytable;

	-- show whats inside the table
	 select * from mytable;
	 
	 