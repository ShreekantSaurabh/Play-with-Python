"""
class FirstClass:
    pass

obj1 = FirstClass()
obj2 = FirstClass()

obj1.x = 5    #dynamically assign a variable of an object
obj2.x = 6

vars(obj1)   # if you have added any data members dynamically or statically then vars will show it
"""
"""
class Point:
    def reset(self):
        self.x = 0
        self.y = 0
        print(self)
        
p1 = Point()
p2 = Point()

p1.x = 1
p1.y = 2
p1.z = 5

p2.x = 3
p2.y = 4

p1.reset()

print(p1.reset())
print(p1.z)
"""

class Point:
    def __init__(self, x, y):
        self.move(x, y)

    def move(self, x, y):
        self.x = 0
        self.y = 0

p1 = Point(3,4)
print(p1.x)

