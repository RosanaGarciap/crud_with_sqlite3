###############################################################
#
#
###############################################################
from studentsdb import built_up_db
from students_record_management import *
import os 

def menu():
        option = 9
        built_up_db()
    
        while option != 0:
                print ( "Student Admin Dashboard" ) 
                print ( "- Enroll new student           (press 1)" ) 
                print ( "- Update Student information   (press 2)" ) 
                print ( "- Delete Student Register      (press 3)" ) 
                print ( "- Search Student Information   (press 4)" ) 
                print ( "- Exit                         (press 0)" ) 
                option = int(input())
                match option:
                        case 1:
                                enroll_student()
                        case 2:
                                update_student_data()
                        case 3:
                                delete_student_register()
                        case 4:
                                search_student_data()
        os.system("cls")
        return
