# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, JSON files, and exception handling
# Change Log:
#   RRoot,1/1/2030,Created Script
#   Kelly Choi, 2/15/2024, Edited Script to adapt to JSON files
# ------------------------------------------------------------------------------------------ #

#import the json package in python

import json
from json import JSONDecodeError

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants - updating this from csv to JSON
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # Holds json data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


#NEW: error handling - the program provides error handling when the file is read
try:
#NEW: when the program starts, the json file is automatically read into a list
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("File must exist in the directory before running the script.")
    print("***Technical Error Message***")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("***Technical Error Message***")
    print(e, e.__doc__, type(e), sep='\n')
except JSONDecodeError as e:
    print("Data in file is not valid. Resetting..")
    print("***Technical Error Message***")
    print(e, e.__doc__, type(e), sep='\n')

    file = open(FILE_NAME, 'w')
    json.dump(students, file)
finally: # this code is executed whether try finishes, or the except finishes
    if not file.closed:
        file.close()  # this would make sure the file is always closed

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("Please select a menu option: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try: #NEW: program provides error handling when numbers are entered
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Please only enter letters.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Please only enter letters.")

            course_name = input("Please enter the name of the course: ")

        #NEW: write into dict, then display the list of dict rows
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue
        except ValueError as e:
            print(e)
            print("***Technical Error Message***")
            print(e.__doc__)

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try: #NEW: program handles errors
            file = open(FILE_NAME, "w")
            #NEW: write to JSON
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("***Technical Error Message***")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("***Technical Error Message***")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
