"""class Father:
    def __init__(self, a,b):
        self.a = a
        self.b = b
        
    def add(a,b,result):
        result = (self.a + self.b)
    
class Mother:
    def __init__(self, a,b,result):
        self.a = a
        self.b = b
        
    def subtract(a,b,result):
        result = (self.a - self.b)

class Son(Father, Mother):
    def mult(a,b, result):
        result = (self.a * self.b)


s1 = Son(3,2)
print (s1.add())"""

class BaseClass():
    num_base_calls = 0
    def call_me(self):
        print("Calling method on base class")
        self.num_base_calls += 1
        print(self.num_base_calls)
        
class LeftClass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on left class")
        self.num_left_calls += 1
        print(self.num_left_calls)
        
class RightClass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on right class")
        self.num_right_calls += 1
        print(self.num_right_calls)

class SubClass(LeftClass, RightClass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on sub class")
        self.num_sub_calls += 1
        print(self.num_sub_calls)
        
b = BaseClass()
l = LeftClass()
r = RightClass()
s = SubClass()

b.call_me()
l.call_me()
r.call_me()
s.call_me()



        
        


    