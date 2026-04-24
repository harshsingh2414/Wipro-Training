from basic_programs.circle import areaofcircle, perimeterofcircle
from basic_programs.basicshapes import areaofrectangle, araeofsquare, perimetreofsquare
radius = int(input("enter the radius: "))
print("area: ", areaofcircle(radius))
print("perimetre: ", perimeterofcircle(radius))

side = int(input("entre side: "))
print("area od square",araeofsquare(side) )
print("perimetre of square: ", perimetreofsquare(side))

length = int(input("entre length: "))
breath = int(input("entre breath: "))
print("area of rectangle: ", areaofrectangle(length, breath))