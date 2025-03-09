###############################################
# MANAGEMENT OF CRUD OPERATIONS OVER DB
# TABLES
###############################################

# Import libraties and functions
import sqlite3
import os
from datetime import datetime as datetime

# build_up function
# Creates the database with its tables, if not exist.
# In case they already exist it retuns a 
# connection
def built_up_db():
    conn = sqlite3.connect("students_record.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS students (
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        gender TEXT NOT NULL,
        address TEXT NOT NULL,
        studentid INTEGER PRIMARY KEY AUTOINCREMENT
        );
        """
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS dismissed (
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        gender TEXT NOT NULL,
        address TEXT NOT NULL,
        dismissed_date TEXT NOT NULL,
        studentid INTEGER PRIMARY KEY
        );
        """
    )

    cursor.close()
    return 

# insert_student
# Creates a new row into the student table
# it represents a new student enrollment
def insert_student(name, lastname, gender, address):

    conn = sqlite3.connect("students_record.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, lastname, gender, address) VALUES(?,?,?,?)", (name, lastname, gender, address))
    conn.commit()
    cursor.close()

# insert_dismiss_student
# Receives as parameter the values of a student row 
# recently deleted. It represents a student that is no
# longer participatin in the program. The cause is indifferent.
def insert_dismiss_student(name, lastname, gender, address, id):
    conn = sqlite3.connect("students_record.db")
    cursor = conn.cursor()
    diss = datetime.now()
    cursor.execute(
        "INSERT INTO dismissed (name, lastname, gender, address, dismissed_date, studentid) VALUES( ?,?,?,?,?,?)", (name, lastname, gender, address, diss, id))
    conn.commit()
    cursor.close()

# show_student
# Given an identification number
# displays in screen the information of the respective student
# and then clean the terminal
def show_student(id):
    
    conn = sqlite3.connect("students_record.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE studentid = ?", (id,))
    row = cursor.fetchone()
    os.system("cls")
    if row:
            print("\nStudent Information")
            print(f"Name:{row[0]}")
            print(f"Lastname:{row[1]}")
            print(f"Gender:{row[2]}")
            print(f"Student ID:{row[3]}")
    else:
            print("ID Number doesn't exist")
    cursor.close()
    conn.close()
    input()

# get_student_row(id)
# given an ID number, it returns the row
# associated with that ID
def get_student_row(id):
    conn = sqlite3.connect("students_record.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE studentid = ?", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row

# update_student_table
# Receives the new values desired to be updated
# into the row associated with the ID number
def update_student_table(name, lastname, gender, address, id):
    conn = sqlite3.connect("students_record.db")
    cursor = conn.cursor()
    cursor.execute('''UPDATE STUDENTS SET name = ?, lastname = ?, gender = ?, address = ? WHERE studentid = ?;''', (name, lastname, gender, address, id)) 
    conn.commit()

    cursor.close() 
    conn.close()

# delete_student_table
# given a ID number, the function deletes the row from the student file
# and ask to store the data into the disnissed table
def delete_student_table(id):
    conn = sqlite3.connect("students_record.db")
    cursor = conn.cursor()
    record = get_student_row(id)
    cursor.execute('''DELETE FROM students WHERE studentid = ?;''', (id,)) 
    conn.commit()

    #Student information is stored as a dissmised student
    insert_dismiss_student(record[0], record[1], record[2], record[3], record[4])

    cursor.close() 
    conn.close()