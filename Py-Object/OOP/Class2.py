#!/usr/bin/python
class Employee:
   'Common base class for all employees'
   empCount = 0
   def __init__(self, name, salary, age):
      self.name = name
      self.salary = salary
      self.age = age
      Employee.empCount += 1
      
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

print "Employee.__doc__:",      Employee.__doc__
print "Employee.__name__:",     Employee.__name__
print "Employee.__module__:",   Employee.__module__
print "Employee.__bases__:",    Employee.__bases__
print "Employee.__dict__:",     Employee.__dict__

E1= Employee("Vikram", 5000, 12)
print "Employee.__doc__:",      E1.__doc__
print "Employee.__module__:",   E1.__module__
#print "Employee.__bases__:",    E1.__bases__
print "Employee.__dict__:",     E1.__dict__
