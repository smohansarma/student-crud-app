# 🧑‍🎓 Student Management System (Python + MySQL)

A console-based CRUD application to manage student records using Python and MySQL.

## 💻 Features
- ➕ Add new student
- 👀 View all students
- 🔁 Update student info
- 🗑️ Delete a student
- 📂 Data saved in MySQL database

## 🛠 Tech Stack
- Python
- MySQL
- mysql-connector-python

## ⚙️ Setup Instructions

### 1. MySQL Table Setup
Run this in MySQL Workbench or CLI:

```sql
CREATE DATABASE school;

USE school;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10),
    email VARCHAR(100)
);


SAMPLE OUTPUT:
=== Student Management System ===
1. Add student
2. View students
3. Update student
4. Delete student
5. Exit
