from math import sqrt, pow


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
        
    @x.setter
    def x(self, new_x):
        raise TypeError("'Point' object does not support coordinate assignment")
        
    @property
    def y(self):
        return self._y
        
    @y.setter
    def y(self, new_y):
        raise TypeError("'Point' object does not support coordinate assignment")
        
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __repr__(self):
        return f"({self._x},{self._y})"
        
    def __str__(self):
        return f"({self._x},{self._y})"
    
    
    
class Line:
    def __init__(self, start, end):
        self._start = start
        self._end = end
        self._length = self._length_calc(self) 
        
    @property
    def start(self):
        return self._start
        
    @start.setter
    def start(self, new_start):
        if not isinstance(new_start, Point):
            raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")
        self._start = new_start
        self._length = self._length_calc(self) 
                   
    @property
    def end(self):
        return self._end
        
    @end.setter
    def end(self, new_end):
        if not isinstance(new_end, Point):
            raise TypeError("'end' attribute of 'Line' object supports only 'Point' object assignment")
        self._end = new_end
        self._length = self._length_calc(self)       
                      
    @property
    def length(self):
        return self._length
        
    @length.setter
    def length(self, new_length):
        raise TypeError("'Line' object does not support length assignment")
        
    def __repr__(self):
        return f"{repr(self._start)}{'\u2501'*3}{repr(self._end)}"
        
    def __str__(self):
        return f"{self._start}{'\u2501'*3}{self._end}"
        
    @staticmethod
    def _length_calc(self):
        return sqrt((pow(self._start.x - self._end.x, 2) + pow(self._start.y - self._end.y, 2)))
        
    
    
class Polygon(list):
    def __init__(self, side1, side2, side3, *side4):
        self.points_list = [side1, side2, side3]
        for line in side4:
            self.points_list.append(line)
    
    @property
    def perimeter(self):
        if not self.__is_closed():
            raise ValueError("line items doesn't form a closed polygon")
        perimeter = 0
        for line in self.points_list:
            perimeter += Line._length_calc(line)
        return perimeter
        
    @perimeter.setter
    def perimeter(self, new_perimeter):
        raise AttributeError("property 'perimeter' of 'Polygon' object has no setter")
        
    def __is_closed(self):
        for i in range(len(self.points_list)):
            if i < len(self.points_list) - 1:
                if self.points_list[i].end != self.points_list[i+1].start:
                    return False
            elif i == len(self.points_list) - 1:
                if self.points_list[i].end != self.points_list[0].start:
                    return False
        return True
        


# >>> p1 = Point(0, 3)
# >>> p2 = Point(4, 0)
# >>> p3 = Point(8, 3)
# >>>
# >>> p1
# (0,3)
# >>> repr(p1) == str(p1)
# True
# >>> p1 == Point(0, 3)
# True
# >>> p1.x, p1.y
# (0, 3)
# >>> p2.y = 5
# Traceback (most recent call last):
  # File "<python-input-8>", line 1, in <module>
    # p2.y = 5
    # ^^^^
  # File "C:\My\Учеба\Kolbin\Kolbin\2024.12.24\1.py", line 23, in y
    # raise TypeError("'Point' object does not support coordinate assignment")
# TypeError: 'Point' object does not support coordinate assignment
# >>>
# >>>
# >>> l1 = Line(p1, p2)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p1)
# >>>
# >>> l1
# (0,3)━━━(4,0)
# >>> repr(l1) == str(l1)
# True
# >>> l1.length
# 5.0
# >>> l1.length = 10
# Traceback (most recent call last):
  # File "<python-input-18>", line 1, in <module>
    # l1.length = 10
    # ^^^^^^^^^
  # File "C:\My\Учеба\Kolbin\Kolbin\2024.12.24\1.py", line 72, in length
    # raise TypeError("'Line' object does not support length assignment")
# TypeError: 'Line' object does not support length assignment
# >>>
# >>> l3.start = 12
# Traceback (most recent call last):
  # File "<python-input-20>", line 1, in <module>
    # l3.start = 12
    # ^^^^^^^^
  # File "C:\My\Учеба\Kolbin\Kolbin\2024.12.24\1.py", line 51, in start
    # raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")
# TypeError: 'start' attribute of 'Line' object supports only 'Point' object assignment
# >>>
# >>>
# >>> pol1 = Polygon(l1, l2, l3)
# >>>
# >>> pol1.perimeter
# 18.0
# >>> pol1.perimeter = 20
# Traceback (most recent call last):
  # File "<python-input-26>", line 1, in <module>
    # pol1.perimeter = 20
    # ^^^^^^^^^^^^^^
  # File "C:\My\Учеба\Kolbin\Kolbin\2024.12.24\1.py", line 103, in perimeter
    # raise AttributeError("property 'perimeter' of 'Polygon' object has no setter")
# AttributeError: property 'perimeter' of 'Polygon' object has no setter
# >>>
# >>> l3.end = Point(-10, -10)
# >>> pol1.perimeter
# Traceback (most recent call last):
  # File "<python-input-29>", line 1, in <module>
    # pol1.perimeter
  # File "C:\My\Учеба\Kolbin\Kolbin\2024.12.24\1.py", line 95, in perimeter
    # raise ValueError("line items doesn't form a closed polygon")
# ValueError: line items doesn't form a closed polygon