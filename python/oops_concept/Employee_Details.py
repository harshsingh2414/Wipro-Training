


class Employee:
     def __init__(self, name, emp_no, basic_pay, hra, da):
         self.__name = name
         self.__emp_no = emp_no
         self.__basic_pay = basic_pay
         self.__hra = hra
         self.__da = da

     def get_name(self):
         return self.__name
     def get_emp_no(self):
         return self.__emp_no
     def get_basic_salary(self):
         return self.__basic_pay
     def set_basic_pay(self, basic):
         self.__basic_pay = basic
     def set_hra(self, hra):
         self.__hra = hra
     def set_da(self, da):
         self.__da = da
     def allowance(self):
         return (self.__hra/100 + self.__da/100) * self.__basic_pay
     def deduction(self):
         return self.__basic_pay*0.1
     def net_salary(self):
         return self.__basic_pay+self.allowance() - self.deduction()
     def show(self):
         print("name: ", self.__name)
         print("emp_no: ", self.__emp_no)
         print("net_salary: ", self.net_salary())
