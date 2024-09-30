# Student Management System

## Overview
The School Management System is a comprehensive Python-based application designed to manage both student and teacher information efficiently. It allows users to store, search, update, and delete records of students and teachers. The system is built with a user-friendly interface using Tkinter, and it connects to a MySQL database to handle data storage. This project is ideal for schools or institutions looking for a streamlined solution to manage their data digitally.

## Features
* Student Management: Add, search, update, and delete student information such as roll number, name, contact details, and more.
* Teacher Management: Add, search, update, and delete teacher information including name, qualifications, CNIC, contact details, and more.
* Interactive UI: Simple and intuitive graphical interface built using Tkinter for easy navigation and data management.
* Search Functionality: Allows for searching by roll number, contact number, CNIC, or name for both students and teachers.
* Responsive Design: The application interface adjusts dynamically to different window sizes, providing a seamless user experience.
* MySQL Database Integration: All records are stored securely in a MySQL database, ensuring data persistence across sessions.

## Main Modules

1. Dashboard
* Quick navigation between Student Area and Teacher Area.
* Access both modules from a unified dashboard.
  
2. Student Management Module
* Add new student records.
* Update existing student details.
* Delete student records.
* Search students by various fields (e.g., Roll Number, Contact, CNIC, Name).
* Display all student records in a table format using Treeview.
  
3. Teacher Management Module
* Add new teacher records
* Update existing teacher details.
* Delete teacher records.
* Search teachers by fields such as Name, CNIC, or Contact Number.
* Display all teacher records in a table format using Treeview.

## Technologies Used
* Python: Core programming language used for application development.
* Tkinter: Used to create the graphical user interface (GUI).
* MySQL: Database system used to store and retrieve student and teacher data.
* pymysql: Python library used for connecting and interacting with the MySQL database.

## How to Use
1. Clone the repository.
2. Install the necessary dependencies.
3. Install the pymysql module.
4. Set up the SQL database.
5. Run the Python script to launch the system.
6. Use the dashboard to navigate between the Student Area and Teacher Area.
7. In the Student Area, you can Add new student records. Search, Update, or Delete Student's data.
8. In the Teacher Area, you can Add new teacher records. Search, Update, or Delete Teacher's data.
