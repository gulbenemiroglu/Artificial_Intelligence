# =============================================================================
#       FUCTIONS
# =============================================================================

def my_function():
  print("Hello from a function")
  
my_function()

# =============================================================================
# Arguments
# =============================================================================
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
# You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")  

  
    
# Arbitrary Keyword Arguments, **kwargs    
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")    
    
    
# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")    
    


# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)    
    
    
# Return Values
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))    
    
    
# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.    
def myfunction():
  pass    


# =============================================================================
#  Positional-Only Arguments
# =============================================================================
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add ",/" after the arguments:
def my_function(x, /):
  print(x)

my_function(3)


# Without the ",/" you are actually allowed to use keyword arguments even if the function expects positional arguments:
def my_function(x):
  print(x)

my_function(x = 3)


# But when adding the ",/" you will get an error if you try to send a keyword argument:
def my_function(x, /):
  print(x)

my_function(x = 3)


# =============================================================================
# Keyword-Only Arguments
# =============================================================================

def my_function(*, x):
  print(x)

my_function(x = 3)


# But with the *, you will get an error if you try to send a positional argument:
def my_function(*, x):
  print(x)

my_function(3)



# =============================================================================
# Combine Positional-Only and Keyword-Only
# =============================================================================
# You can combine the two argument types in the same function.
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
my_function(5, b=6, c = 7,d= 8) #TypeError: my_function() got some positional-only arguments passed as keyword arguments: 'b'
my_function(5, b=6,7,d= 8) #SyntaxError: positional argument follows keyword argument


# =============================================================================
# Recursion
# =============================================================================
# Python also accepts function recursion, which means a defined function can call itself.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
# 6+f(5)=15 => 21
# 5+f(4)=10 => 15
# 4+f(3)=6  => 10
# 3+f(2)=3  => 6
# 2+f(1)=1  => 3
# 1+f(0)=0  => 1





    
    
    
