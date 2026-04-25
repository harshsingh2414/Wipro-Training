from oops_concept.college import College

class Student(College):
    def __init__(self, code, city, name, stname, rollno, marks):
        super().__init__(code, city, name)
        self.stname = stname
        self.rollno = rollno
        self.marks = marks

    def display_student_details(self):
        print(f'Student name: {self.stname}\n'
              f'Roll number: {self.rollno}\n'
              f'Marks: {self.marks}')