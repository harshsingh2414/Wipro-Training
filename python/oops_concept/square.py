from oops_concept.formulamethods import FM

class Square(FM):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side*self.side
    def calculate_perimetre(self):
        return self.side*4