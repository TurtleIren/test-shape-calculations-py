import sys
import re
import math

class TwoDShape:
    def __init__(self, line):
        self.line = line
        self.shape = ''

    def calc_perimeter_and_area(self):
        return "Unknown shape"

#get point coordinates from line by mask
    def get_coordinates(self, pointMask):
        try:
            coordsPoint = re.search(pointMask + ' (-?\d+) (-?\d+)( |$)', self.line)
            if coordsPoint:
                x = int(coordsPoint.group(1))
                y = int(coordsPoint.group(2))
                #print(x, y, "Ok")
                return (x, y)
        except:
            raise Exception("there is no coords values")


    def print_output(self, shape, perimeter, area):
        print(shape, 'Perimeter', perimeter, 'Area', area)
        return

    def check_shape(self):
        is_correct = re.search(r"^" + self.shape + r"\b", self.line)
        return is_correct
  
#calculate P & A for Square
#Example string:
#Square TopRight 1 1 Side 1
class Square(TwoDShape):
    def __init__(self, line):
        self.line = line
        self.shape = 'Square'
    
    def calc_perimeter_and_area(self):
        try:
            sideSearch = re.search('Side (\d+$)', self.line)
            if sideSearch:
                side = int(sideSearch.group(1))
                perimeter = 4 * side
                area = side ** 2

                self.print_output('Square', perimeter, area)
                return ""
            else:
                return "Error: there is no Side value"
        except:
            return "Error: there is no Side value"

#calculate P & A for Rectangle
#Example string:
#Rectangle TopRight 2 2 BottomLeft 1 1
class Rectangle(TwoDShape):
    def __init__(self, line):
        self.line = line
        self.shape = 'Rectangle'
    
    def calc_perimeter_and_area(self):
        try:
            x1, y1 = self.get_coordinates('TopRight')
        except:
            return "Error in TopRight coordinates"
    
        try:
            x2, y2 = self.get_coordinates('BottomLeft')
        except:
            return "Error in BottomLeft coordinates"

        if x1 < x2 or y1 < y2:
            return "Error: Coordinates are not in correct sequence"
        
        perimeter = 2 * (abs(x2 - x1) + abs(y2 - y1))
        area = abs(x2 - x1) * abs(y2 - y1)
    
        self.print_output('Rectangle', perimeter, area)
        return ""

#calculate P & A for Circle
#Example string:
#Circle Center 1 1 Radius 2
class Circle(TwoDShape):
    def __init__(self, line):
        self.line = line
        self.shape = 'Circle'
    
    def calc_perimeter_and_area(self):
            
        try:
            radiusSearch = re.search('Radius (\d+$)', self.line)
            if radiusSearch:
                radius = int(radiusSearch.group(1))
            
                perimeter = 2 * math.pi * radius
                area = math.pi * radius ** 2
    
                self.print_output('Circle', perimeter, area)
                return ""
            else:
                return "Error: there is no correct Radius value"
                
        except:
            return "Error: there is no Radius value"

#main procedure
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    if "Square" in line:
        shape = Square(line)
    elif "Rectangle" in line:
        shape = Rectangle(line)
    elif "Circle" in line:
        shape = Circle(line)
    else:
        #print('Unknown shape')
        shape = TwoDShape(line)

    if shape.check_shape():    
        print(shape.calc_perimeter_and_area())
    else:
        print("Error: bad string format for " + shape.shape)

