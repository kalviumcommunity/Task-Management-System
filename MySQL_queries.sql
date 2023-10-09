-- DDL commands (Data Definition Language) for creating database and tables

-- Create the database
CREATE DATABASE TaskManagementDB;

-- Use the created database
USE TaskManagementDB;

-- Create the User table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    salt VARCHAR(255)
);

-- Create the Task table
CREATE TABLE Tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    task_description TEXT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create the Task_details table
CREATE TABLE Task_details (
    task_id INT PRIMARY KEY,
    due_date DATE,
    priority VARCHAR(255),
    tag VARCHAR(255),
    archived BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id)
);

-- Create the Task_status table
CREATE TABLE Task_status (
    task_id INT PRIMARY KEY,
    status VARCHAR(255) DEFAULT 'todo',
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id)
);

-- DML commands (Data Manipulation Language) for inserting and updating data

-- Insert data into the Users table
INSERT INTO Users (username, email, password, salt)
VALUES ('john_doe', 'john@example.com', 'hashed_password', 'random_salt');

-- Insert data into the Tasks table
INSERT INTO Tasks (task_description, user_id)
VALUES ('Complete project report', 1);

-- Insert data into the Task_details table
INSERT INTO Task_details (task_id, due_date, priority, tag, archived)
VALUES (1, '2023-11-15', 'High', 'Work', FALSE);

-- Insert data into the Task_status table
INSERT INTO Task_status (task_id, status)
VALUES (1, 'todo');

-- Update the status of the task to "in progress"
UPDATE Task_status
SET status = 'in progress'
WHERE task_id = 1;
