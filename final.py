"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name :Nada Iyad El_khatib
Delivery Date :22/6/2023
"""


# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)



import uuid

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

             
course_name = input("Enter the course name: ")
course_mark = float(input("Enter the course mark: "))

course = Course(course_name, course_mark)

import uuid
class Student:
    # TODO 3 define static variable indicates total student count
    total_student_count = 0


    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)

    def __init__(self, student_name, student_age, student_number, courses_list):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list

        Student.total_student_count += 1

    # TODO 5 define a method to enroll new course to student courses list

    def enroll_course(self, course):
        self.courses_list.append(course)

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        return self.courses_list
        # TODO 6 print student courses with their marks

    def print_student_courses(self):
        for course in self.courses_list:
            print("Course Name:", course.course_name)
            print("Course Mark:", course.course_mark)
            print()

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        total_marks = 0
        for course in self.courses_list:
            total_marks += course.course_mark

        if len(self.courses_list) > 0:
            average = total_marks / len(self.courses_list)
        else:
            average = 0

        return average


# in Global Scope
# TODO 8 declare empty students list
students = []

while True:


    # TODO 9 handle Exception for selection input
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. Exit" ))

        if selection == 1:
    

        # TODO 10 make sure that Student number is not exists before
        student_number = input("Enter Student Number")
        exists = False
        for student in students:
            if student.student_number == student_number:
                exists = True
                break

        if exists:
            print("Student number exists , enter another number .")
        else:
            break

        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

        # TODO 11 create student object and append it to students list
        new_student = Student(student_name, student_age, student_number, [])
        students.append(new_student)

        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses

    else:
        # TODO 16 call a function to exit the program
        pass