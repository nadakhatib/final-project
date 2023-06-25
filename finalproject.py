import uuid
import sys


class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = str(uuid.uuid4())
        self.course_name = course_name
        self.course_mark = course_mark


course_name = input("Enter the course name: ")
course_mark = float(input("Enter the course mark: "))

course = Course(course_name, course_mark)


class Student:
    total_student_count = 0

    def __init__(self, student_name, student_age, student_number, courses_list):
        self.student_id = str(uuid.uuid4())
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = courses_list

        Student.total_student_count += 1

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def print_student_courses(self):
        for course in self.courses_list:
            print("Course Name:", course.course_name)
            print("Course Mark:", course.course_mark)
            print()

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        if len(self.courses_list) > 0:
            average = total_marks / len(self.courses_list)
        else:
            average = 0

        return average


students = []


def exit_program():
    print("Exiting the program...")
    sys.exit()


while True:
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. Exit\n"
                              "Enter your selection: "))

        if selection == 1:
            student_number = input("Enter Student Number: ")
            exists = False
            for student in students:
                if student.student_number == student_number:
                    exists = True
                    break

            if exists:
                print("Student number exists, enter another number.")
            else:
                student_name = input("Enter Student Name: ")
                while True:
                    try:
                        student_age = int(input("Enter Student Age: "))
                        break
                    except ValueError:
                        print("Invalid value. Please enter a valid integer for the student age.")

                new_student = Student(student_name, student_age, student_number, [])
                students.append(new_student)

                print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number: ")
            found = False
            for student in students:
                if student.student_number == student_number:
                    found = True
                    students.remove(student)
                    print("Student Deleted Successfully")
                    break

            if not found:
                print("Student Not Exist")

        elif selection == 3:
            student_number = input("Enter Student Number: ")
            found = False
            for student in students:
                if student.student_number == student_number:
                    found = True
                    student_details = student.get_student_details()
                    print("Student Details:")
                    for key, value in student_details.items():
                        print(f"{key}: {value}")
                    break

            if not found:
                print("Student Not Exist")

        elif selection == 4:
            student_number = input("Enter Student Number: ")
            found = False
            for student in students:
                if student.student_number == student_number:
                    found = True
                    student_average = student.get_student_average()
                    print(f"Student Average: {student_average}")
                    break

            if not found:
                print("Student Not Exist")

        elif selection == 5:
            student_number = input("Enter Student Number: ")
            found = False
            for student in students:
                if student.student_number == student_number:
                    found = True
                    course_name = input("Enter Course Name: ")
                    course_mark = float(input("Enter Course Mark: "))
                    new_course = Course(course_name, course_mark)
                    student.courses_list.append(new_course)

                    print("Course Added to Student Successfully")
                    break

            if not found:
                print("Student Not Exist")

        elif selection == 6:
            exit_program()

    except ValueError:
        print("Invalid input. Please enter a valid integer for the selection.")
