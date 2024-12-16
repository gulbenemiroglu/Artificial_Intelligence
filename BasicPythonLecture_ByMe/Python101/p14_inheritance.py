# =============================================================================
#       INHERITANCE
# =============================================================================

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# Create a Child Class
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()



class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# Use the super() Function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# Add Properties
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

