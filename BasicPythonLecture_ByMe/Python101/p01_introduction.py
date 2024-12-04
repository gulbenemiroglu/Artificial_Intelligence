
#RUN SELECTION OR CURRENT LINE/LINES
print("hello ai era!")

# =====================
#  PYTHON INDENTATION
# =====================

#  Correct Indentation Example:
if 5 > 2:
    print("Beş, ikiden büyüktür!")
    
#  Incorrect Indentation Example:
if 5 > 2:
print("Beş, ikiden büyüktür!")  # Missing indentation 


# =====================
#   PYTHON VARIABLES
# =====================

x = 10                  #int
y = "Merhaba, Dünya!"   #str
print(x)
print(y)

#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"



# Camel Case -> Each word, except the first, starts with a capital letter:
myVariableName = "John"
# Pascal Case -> Each word starts with a capital letter:
MyVariableName = "John"
# Snake Case -> Each word is separated by an underscore character:
my_variable_name = "John"


# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Global Variables -> Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# -------------------------------------------------

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# -------------------------------------------------

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# -------------------------------------------------

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# =====================
#    PYTHON COMMENTS
# =====================
# print("Hello, World!")  # This code will not execute.
print("Cheers, Mate!")  # This code will execute.

#This is a comment
#written in
#more than just one line
print("Hello, World!")


"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")







