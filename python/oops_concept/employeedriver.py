from oops_concept.Employee_Details import Employee

name = input("name:")
emp_no = int(input("employee_no: "))
basic_pay = int(input("basic pay: "))
hra = int(input("hra: "))
da = int(input("da: "))

emp = Employee(name,emp_no, basic_pay, hra, da)
emp.set_basic_pay(basic_pay + 10000)
emp.show()
