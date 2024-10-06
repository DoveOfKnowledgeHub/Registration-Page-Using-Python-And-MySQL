# Registration-Page-Using-Python-And-MySQL

This project is a graphical user interface (GUI) application developed using Python's Tkinter library, integrated with a MySQL database for effective data management. 
Before running the application, ensure that all necessary modules are installed as outlined in the requirements.txt file.

To set up the project, follow these essential steps:
1. Create a database named "user_registration".
2. Within this database, establish a table called "users".

use this code to create the table under the "user_registration" database
 
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,            -- Unique identifier for each user
    email VARCHAR(255) NOT NULL UNIQUE,           -- User's email, must be unique
    username VARCHAR(255) NOT NULL UNIQUE,        -- User's username, must be unique
    password VARCHAR(255) NOT NULL                 -- User's password
);
