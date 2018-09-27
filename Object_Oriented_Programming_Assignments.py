# 1. Fill in the Line class methods to accept coordinate as a
#     pair of tuples and return the slope and distance of the line.

class Line(object):

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        dx = x2 - x1
        dy = y2 - y1
        dsquared = dx**2 + dy**2
        result = dsquared ** 0.5
        return result

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return (y2-y1)/(x2-x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print("The Distance between the two co ordinates are : ", li.distance())

print("The Distance between the slope is : ", li.slope())

# 2. Fill in the class

class Cylinder(object):

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        return 3.14 * self.radius * self.radius * self.height

    def surface_area(self):
        return (2 * 3.14 * self.radius * self.height) + (2 * 3.14 * self.radius * self.radius)


c = Cylinder(2, 3)

print("The Volume of the cylinder is : ", c.volume())

print("The Surface Area of the cylinder is : ", c.surface_area())