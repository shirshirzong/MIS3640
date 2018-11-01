import math

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

jack = Point() #jack is an object of Point
# print(type(jack))

jack.x = 3
jack.y = 4
# on x axis jack is at 3, y axis at 4

# print(jack.x, jack.y)

# x = jack.y
# print(x)
# print(jack.x)
jonathan = Point()
jonathan.x = 50
jonathan.y = 50

def print_point(p):
    """Print a Point object in human-readable format."""
    print('({}, {}).'.format(p.x, p.y))

print_point(jack)
print_point(jonathan)

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    x_diff = p2.x - p1.x
    y_diff = p2.y - p2.y
    distance = math.sqrt(x_diff**2 + y_diff**2) #x^2+y^2=z^2
    return distance

print(distance_between_points(jack,jonathan))




class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

angela = Rectangle()
angela.width = 100
angela.height = 100
angela.corner = jack #corner is the point to represent the position


def find_center(rect):
    """Returns a Point at the center of a Rectangle.

    rect: Rectangle

    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

sarah = find_center(angela)
print_point(sarah)

# angela.width = box.width + 50
# angela.height = box.height + 100

def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.

    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight
    
print(angela.width)
print(angela.height)
print('grow')
grow_rectangle(angela, 50, 100)
print(angela.width)
print(angela.height)




def print_rectangle(rect):
    print('width:', rect.width, 'height:', rect.height)
    print('the lower-left corner:')
    print_point(rect.corner)

print_rectangle(angela)


def main():
    my_point = Point()
    # print(Point.__doc__)
    # my_point.x = 3
    # my_point.y = 4
    # print('My point', end=' ')
    # print_point(my_point)

    # print('Is my_point an instance of Point?', isinstance(my_point, Point))
    # print('Is my_point an instance of Rectangle?',
    #       isinstance(my_point, Rectangle))
    # print('Does my_point have an attribute x?', hasattr(my_point, 'x'))
    # print('Does my_point have an attribute z?', hasattr(my_point, 'z'))

    # box = Rectangle()
    # box.width = 100.0
    # box.height = 200.0
    # box.corner = Point()
    # box.corner.x = 0.0
    # box.corner.y = 0.0

    # print('Does box have an attribute x?', hasattr(box, 'x'))

    # print('Does box have an attribute corner?', hasattr(box, 'corner'))

    # print('Rectangle has these:', dir(box))

    # center = find_center(box)
    # print('center', end=' ')
    # print_point(center)

    # print(box.width)
    # print(box.height)
    # print('grow')
    # grow_rectangle(box, 50, 100)
    # print(box.width)
    # print(box.height)


if __name__ == '__main__':
    main()
