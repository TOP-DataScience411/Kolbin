from math import pow, sqrt

class Tetrahedron:
    def __init__(self, edge):
        self.edge = float(edge)
        
    def surface(self):
        square = sqrt(3) * pow(self.edge, 2)
        return square
    
    def volume(self):
        vol = pow(self.edge, 3) / 12 * sqrt(2)
        return vol
    
    
    
# >>> t1 = Tetrahedron(5)
# >>> t1.edge
# 5.0
# >>> t1.surface()
# 43.30127018922193
# >>> t1.volume()
# 14.73139127471974
# >>> t1.edge = 6
# >>> t1.surface()
# 62.35382907247958