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
      print "Name : ", self.name,  ", Salary: ", self.salary, "Age:", self.age

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000, 4)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000, 6)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount


if (hasattr(emp2, 'age')):
    print "Age Found"
    # Returns true if 'age' attribute exists
getattr(emp2, 'age')    # Returns value of 'age' attribute
setattr(emp2, 'age', 8) # Set attribute 'age' at 8
delattr(emp2, 'age')    # Delete attribute 'age'


