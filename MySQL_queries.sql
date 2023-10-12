CREATE DATABASE TaskManagementDB;

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