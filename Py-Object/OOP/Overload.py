#!/usr/bin/python

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

   def __repr__(self):
       return self.a, self.b

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2).__str__()

print v1.__repr__()
print v2.__str__()