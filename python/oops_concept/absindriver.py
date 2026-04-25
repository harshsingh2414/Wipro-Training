from oops_concept.square import Square
from oops_concept.rectangle import Rectangle

sobj = Square(10)
robj = Rectangle(10,20)
print(f'area of square: {sobj.calculate_area()} \n perimetre of square: {sobj.calculate_perimetre()}')
print(f'area of rectangle: {robj.calculate_area()} \n perimetre of rectangle: {robj.calculate_perimetre()}')