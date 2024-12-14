# =============================================================================
#       CLASSES/OBJECTS
# =============================================================================

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)



# =============================================================================
# Class Attributes 
# =============================================================================
class DataScientist():
    department = " "
    sql ="Yes"
    experience = 0
    languages = []

DataScientist.department
DataScientist.sql

DataScientist.sql="No"
DataScientist.sql #Out: 'No'

person1= DataScientist()
person1.department
person1.sql
person1.experience
person1.languages.append("Eng")
person1.languages

person2= DataScientist()
person2.department
person2.sql
person2.experience
person2.languages      #but person2 doesnt know Eng. This is a problem.



# =============================================================================
# The __init__() Function
# =============================================================================

class DataScientist():
    def __init__(self):
        self.languages = []
        

person1 = DataScientist()
person1.languages.append('Eng')


person2 = DataScientist()
person2.languages.append('Python')

person1.languages         # ['Eng']
person2.languages         # ['Python']
DataScientist.languages   # AttributeError: type object 'DataScientist' has no attribute 'languages'


# !! self ifadesi sadece instancelar için kullanılan bir özelliktir
# Eğer sınıfın özelliklerine erişmek istiyorsak bunu kendi içinde tanımlamamız gerekir.


class DataScientist():
    department = ""
    sql ="Yes"
    experience = 0
    languages = ['Python','R','JS']
    def __init__(self):
        self.department = " "
        self.languages = []

emp1 = DataScientist()
emp2 = DataScientist()

emp1.languages
emp2.languages
DataScientist.languages


#	correct usage
class DataScientist():
    employees=[]
    def __init__(self):
        self.department = " "
        self.languages = []
    def add_languges(self,new_language):
        self.languages.append(new_language)

employee_1 = DataScientist()
employee_2 = DataScientist()

employee_1.add_languges('Python')
employee_2.add_languges('R')

employee_1.languages
employee_2.languages


# =============================================================================
# The __str__() Function
# =============================================================================


# The __str__() function controls what should be returned when the class object is represented as a string.

# WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

# WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


# =============================================================================
# Object Methods
# =============================================================================

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.







