# Name: Abiola Flourish
# File Name: student_records.py
# This program accepts student names and GPAs
# and determines whether students qualify for the Dean's List
# or the Honor Roll.

while True:
    last_name = input("Enter student's last name (ZZZ to quit): ")

    if last_name == "ZZZ":
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List!")

    if gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll!")

    if gpa < 3.25:
        print(first_name, last_name, "does not qualify for either list.")

    print()

# last_name	Stores the student's last name 
# Also checks whether the user entered "ZZZ" to stop the program.
# first_name Stores the student's first name.
# gpa Stores the student's GPA as a decimal number. 
# Used to determine whether the student qualifies for the Dean's List or Honor Roll.