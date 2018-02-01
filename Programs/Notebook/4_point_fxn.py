class Point:
    def reset(self):
        self.x = 0
        self.y = 0
        print self


p1 = Point()
p2 = Point()

print p1
print p2

p1.x = 100
p1.y = 300

p2.x = 34
p2.y =90

#print(p.x, p.y)
#print(p1.x, p1.y)

print "calling reset in point class"
p1.reset()
#print(p.x, p.y)


p2.reset()
#print(p1.x, p1.y)

