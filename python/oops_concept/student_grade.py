from oops_concept.student import Student

class StudentGrade(Student):
    def __init__(self, code, city, name, stname, rollno, marks):
        super().__init__(code, city, name, stname, rollno, marks)

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def display_grade(self):
        grade = self.calculate_grade()
        print(f'Student name: {self.stname}\n'
              f'Roll number: {self.rollno}\n'
              f'Marks: {self.marks}\n'
              f'Grade: {grade}')
