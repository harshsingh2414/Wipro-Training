class College:
    def __init__(self, code, city, name):
        self.college_code = code
        self.college_city = city
        self.college_name = name
    def welecome_message(self):
        print("Hello There")
    def display_college_details(self):
        print(f'college code:{self.college_code}\n college name: {self.college_name} \n college city: {self.college_city}')

