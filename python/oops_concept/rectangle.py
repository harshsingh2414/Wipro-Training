from oops_concept.formulamethods import FM
class Rectangle(FM):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calculate_area(self):
        return self.l*self.b
    def calculate_perimetre(self):
        return 2*(self.l+self.b)
