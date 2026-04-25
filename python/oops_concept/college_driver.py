from oops_concept.college import College
from oops_concept.student import Student
from oops_concept.student_grade import StudentGrade
from oops_concept.teacher import Teacher

cc = int(input("college code: "))
cci = input("college city: ")
cn = input("college name: ")
# rno = int(input("entre roll no: "))
# stname = input("enter student name")
# stmarks = int(input("marks: "))
t_name = input("entre teacher name")
e_id = int(input("entre employee id"))
t_dept = input("entre teacher department")
basic_pay = float(input("entre basic pay"))

# project = College(cc, cci, cn)
# project.welecome_message()
# project.display_college_details()



# project = Student(cc, cci, cn, stname, rno, stmarks)
# project.display_college_details()
# project.display_student_details()

# project = StudentGrade(cc, cci, cn, stname, rno, stmarks)
# project.display_grade()

project = Teacher(cc,cci,cn,e_id, t_name, t_dept, basic_pay)
project.show()