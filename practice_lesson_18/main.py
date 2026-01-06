from student import Student


def main():
    # Create an instance of Student
    student_1 = Student("Alice", 20, "S12345")
    student_2 = Student("Bob", 19, "S111111")
    student_3 = Student("Charlie", 21, "S67890", "Charlie@gmail.com")

    # Get and print student information
    students = [student_1, student_2, student_3]

    for student in students:
        print(student.get_info())


if __name__ == "__main__":
    main()