###############################################################
#
#
###############################################################
from studentsdb import insert_student, show_student, get_student_row, update_student_table,delete_student_table
import os

def update_student_form():

    print ("Inserte el ID estudiantil (example 1100000)")
    student_id = input()

def enroll_student():
    print("Ingrese los siguientes campos:")
    name = input("Name:")
    lastname = input("Lastname:")
    gender = ""
    while (gender != "F" and gender != "M"):
        gender = input("Gender (press F or M):")
    address = input("Address:")
    insert_student(name, lastname, gender, address) 

def search_student_data():
    id = int(input("Insert ID number: "))
    show_student(id)

def update_student_data():

    #Search Row
    id = int(input("Insert ID number: "))
    original_row = get_student_row(id)

    #Original values
    print("CURRENT VALUES")
    print("\n Ingrese los siguientes campos: \n")
    name = original_row[0]
    lastname = original_row[1]
    gender = original_row[2]
    address = original_row[3]
    stop = -1

    while stop != 0:
        print ( "What action you want to do:" ) 
        print ( "- Change name       (press 1)" ) 
        print ( "- Change lastname   (press 2)" ) 
        print ( "- Change gender     (press 3)" ) 
        print ( "- Change address    (press 4)" ) 
        print ( "- Exit              (press 0)" ) 
        option = int(input())

        match option:
                case 0: break
                case 1:
                        name = input("Insert name: ")
                case 2:
                        lastname = input("Insert name: ")
                case 3:
                        gender = ""
                        while (gender != "F" and gender != "M"):
                            gender = input("Gender (press F or M):")
                case 4:
                        address = input("Address:")
    update_student_table(name, lastname, gender, address, id)

def delete_student_register():
    id = int(input("Insert ID number: "))
    show_student(id)
    delete = input("Are you sure you want to delete this register? (press y or n)")
    while (delete != "y" and delete != "n"):
        delete = input("Invalid option, please press y (yes) or n (no):")
        
    if delete == "y":
         delete_student_table(id)
