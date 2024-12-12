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