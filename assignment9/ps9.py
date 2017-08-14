# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")
    
class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
class Triangle(Shape):
    def __init__(self, b, h):
        self.height = float(h)
        self.base = float(b)
    def area(self):
        return self.base * self.height
    def __str__(self):
        return 'Triangle with  base' + str(self.base) + ' and height' + str(self.height)
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same height and base.
        other: object to check for equality
        """
        return type(other) == Triangle and self.height == other.height and self.base == other.base


#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """

        self.shape = []
        
    def addShape(self, sh):
                """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
                if sh not in self.shape:
                    self.shape.append(sh)
        
 
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        for x in self.shape:
            yield x
      
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        string = ""
        for x in self.shape:
            string = string + str(x) + "\n"
        return string



        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    #find the object with the biggest area
    #note this will return only one object that's why we need to check
    #if there is other objects with the same area so we can add them to the tuble
    maxArea = max(shapes, key=lambda shape: shape.area())
    shapesAreas = []
    shapesAreas.append(maxArea)
    
    for shape in shapes:
        if shape.area() == maxArea.area():
            if shape != maxArea:
                shapesAreas.append(shape)
    return shapesAreas
    
ss = ShapeSet()
t = Triangle(4,6)
ss.addShape(Circle(1))
ss.addShape(t)
ss.addShape(Triangle(3,8))
largest = findLargest(ss)
for e in largest:
    print e


    

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    #initiate shape set
    shapeSet = ShapeSet()
    #open the file
    inputFile = open(filename)
    #loop over the file
    for line in inputFile:
        #remove the white space from eachline
        line = line.strip()
        #split the line to a list of items
        line = line.split(',')
        if line[0].lower() == 'circle':
            shape = Circle(line[1])
        if line[0].lower() == 'triangle':
            shape = Triangle(line[1],line[2])
        if line[0].lower() == 'square':
            shape = Square(line[1])
        shapeSet.addShape(shape)
        
    return shapeSet
    

ss = readShapesFromFile('shapes.txt')
print ss

    
