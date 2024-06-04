import sys
import re
import math

#calculate P & A for Square
#Example string:
#Square TopRight 1 1 Side 1
def square(line):
    try:
        #sideSearch = re.search('Side (.+?)', line)
        sideSearch = re.search('Side ([\d]+$)', line)
        if sideSearch:
            side = int(sideSearch.group(1))
            perimeter = 4 * side
            area = side ** 2

            print_output('Square', perimeter, area)
            return ""
        else:
            return "Error: there is no Side value"
    except:
        return "Error: there is no Side value"

    
#get point coordinates from line by mask
def get_coordinates(pointMask, line):
    try:
        coordsPoint = re.search(pointMask + ' ([\d]+) ([\d]+)( |$)', line)
        if coordsPoint:
            x = int(coordsPoint.group(1))
            y = int(coordsPoint.group(2))
            return (x, y)
    except:
        raise Exception("there is no coords values")
        return (0, 0)
    
#calculate P & A for Rectangle
#Example string:
#Rectangle TopRight 2 2 BottomLeft 1 1
def rectangle(line):
    try:
        x1, y1 = get_coordinates('TopRight', line)
    except:
        return "Error in TopRight coordinates"
    
    try:
         x2, y2 = get_coordinates('BottomLeft', line)
    except:
        return "Error in BottomLeft coordinates"
   
    perimeter = 2 * (abs(x2 - x1) + abs(y2 - y1))
    area = abs(x2 - x1) * abs(y2 - y1)
    
    print_output('Rectangle', perimeter, area)
    return ""

#calculate P & A for Circle
#Example string:
#Circle Center 1 1 Radius 2
def circle(line):
    try:
        radiusSearch = re.search('Radius ([\d]+$)', line)
        if radiusSearch:
            radius = int(radiusSearch.group(1))
            
            perimeter = 2 * math.pi * radius
            area = math.pi * radius ** 2
    
            print_output('Circle', perimeter, area)
            return ""
        else:
            return "Error: there is no Radius value"
    except:
        return "Error: there is no Radius value"

    
def print_output(shape, perimeter, area):
    print(shape, 'Perimeter', perimeter, 'Area', area)
    return


#main procedure
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    #print(f'Processing Message from sys.stdin *****{line}*****')

    if "Square" in line:
        print(square(line))
    elif "Rectangle" in line:
        print(rectangle(line))
    elif "Circle" in line:
        print(circle(line))
    else:
        print('Unknown shape')
        
print("Done")

