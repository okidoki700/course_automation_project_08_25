class Student:
    def __init__(self, name, age, student_id, email=None):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.email = email

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}, Email: {self.email if self.email else 'N/A'}"