#CARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTER 

import math 

class Point:
    def __init__(self, point_x: int, point_y: int):
        self.point_x = point_x
        self.point_y = point_y

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
        

    def compute_length(self) -> float:
        x = self.end.point_x - self.start.point_x
        y = self.end.point_y - self.start.point_y
        return math.sqrt(x**2 + y**2)
    
    def compute_slope(self) -> float:
        x = self.end.point_x - self.start.point_x
        y = self.end.point_y - self.start.point_y

        if x == 0:
            return 90.0
    
        return  math.degrees(math.atan2(y,x))
    
    def compute_horizontal_cross(self):
        y1 = self.start.point_y
        y2 = self.end.point_y
        if y1 * y2 <= 0:
            return True
        else:
            return False

    def compute_vertical_cross(self):
        x1 = self.start.point_x
        x2 = self.end.point_x
        if x1 * x2 <= 0:
            return True
        else:
            return False

#CARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTER

class Rectangle:
    def __init__(self, method: int, p1 = None, p2 = None, width = None, 
                 height = None, center = None, lines = None):
        
        if method == 1:
            self.width = width
            self.height = height
            self.bottom_left = p1

            self.center = Point(p1.point_x + width / 2, 
                                p1.point_y + height / 2)

        elif method == 2:
            self.center = p1
            self.width = width
            self.height = height

            self.bottom_left = Point(p1.point_x - width / 2,
                                     p1.point_y - height / 2)

        elif method == 3:
            self.width = abs(p2.point_x - p1.point_x)
            self.height = abs(p2.point_y - p1.point_y)
            self.center = Point((p1.point_x + p2.point_x) / 2, 
                                (p1.point_y + p2.point_y) / 2
            )
        elif method == 4:
            self.lines = lines  # lista de 4 líneas

    
            self.bottom_left = lines[0].start
            self.width = lines[0].compute_length()
            self.height = lines[1].compute_length()

        # Centro siempre calculado
        self.center = Point(
            self.bottom_left.point_x + self.width / 2,
            self.bottom_left.point_y + self.height / 2
        )
    
    def compute_area(self):
        return self.width * self.height 
    
    def compute_perimeter(self):
        return 2 * (self.width + self.height)
    
    def compute_interference_point(self, point: Point):
        x_min = self.center.point_x - self.width / 2
        x_max = self.center.point_x + self.width / 2
        y_min = self.center.point_y - self.height / 2
        y_max = self.center.point_y + self.height / 2

        if x_min <= point.point_x <= x_max and y_min <= point.point_y <= y_max:
            return True
        else:
            return False
    
class Square(Rectangle):
    def __init__(self, method, p1=None, p2=None, width=None, height=None, center=None):
        super().__init__(method, p1, p2, width, height, center)

    def compute_area(self):
        return self.width ** 2
    
    def compute_perimeter(self):
        return 4 * self.width
    


  
