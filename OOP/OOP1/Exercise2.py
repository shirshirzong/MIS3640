import math
import copy



class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b   
    
    def __str__(self):
        """return a Point object in human-readable format."""
        return '({}, {}).'.format(self.x, self.y)



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



class Circle:
    """Represents a circle. 

    attributes: center, radius.
    """



# def point_in_circle(cir):
#     '''Returns True if a Point lies in or on the boundary of the Circle.

#     cir: Circle

#     returns: True/False
#     '''
#     p = Point()
#     p.x = int(input('Please enter x coordinate of the point'))
#     p.y = int(input('Please enter y coordinate of the point'))
    
#     center = cir.center
#     if distance_between_points(center, p) > cir.radius:
#         return False
#     else: 
#         return True

# print(point_in_circle(cirshir))    

def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).
    point: Point object
    circle: Circle object
    """
    d = distance_between_points(point, circle.center)
    # print(d)
    return d <= circle.radius


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """



def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.
    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner) #so it doesn't change the original corner object
    print(p)
    if not point_in_circle(p, circle):
        return False

    p += rect.width
    print(p)
    if not point_in_circle(p, circle):
        return False
    
    p.y += rect.height
    print(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print(p)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):

    """Checks whether any corners of a rect fall in/on a circle.
    rect: Rectangle object
    circle: Circle object
    """

    #as long as one corner falls in/on a circle, return True
    p = copy.copy(rect.corner)
    print(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print(p)
    if point_in_circle(p, circle):
        return True

    p.y += rect.height
    print(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print(p)
    if point_in_circle(p, circle):
        return True

    return False



def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()