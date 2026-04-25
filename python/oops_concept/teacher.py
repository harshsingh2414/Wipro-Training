from token import tok_name

from oops_concept.college import College
from oops_concept.employeedriver import basic_pay


class Teacher(College):
    def __init__(self, code, city, name, eid, tname, tdept, basic_pay):
        self.eid = eid
        self.tname = tname
        self.tdept = tdept
        self.basicpay = basic_pay
    def calcu_salary(self):
        print(f'salary: {self.basicpay + self.basicpay * 0.1}')
    def show(self):
        print(f'city: {self.college_city}\ncollege name {self.college_name}\ndepartment: {self.tdept}\n teacher id:{self.eid}\nteacher name: {self.tname}')
