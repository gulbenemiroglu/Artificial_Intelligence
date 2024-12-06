# =============================================================================
#       TUPLES
# =============================================================================
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# =============================================================================
# LISTS IS:
# 
# ORDERED (indexed)
# UNCHANGABLE!!! (we CANNOT change, add, and remove items)
# ALLOW DUPLICATES (items could be the same value)
# =============================================================================


# Tuple Length - len() function
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple, it is str
thistuple = ("apple") 
print(type(thistuple))

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

# type()
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


# The tuple() Constructor
# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
  
# =============================================================================
# Update Tuples
# =============================================================================

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# =============================================================================
# Add Items
# =============================================================================

# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# 2. Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# =============================================================================
# Remove Items
# =============================================================================

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# Convert the tuple into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Or you can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
thistuple = ("apple", "banana", "cherry")
print(thistuple) #this will raise an error because the tuple no longer exists


# =============================================================================
# Unpack Tuples
# =============================================================================

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Packing a tuple:

fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# Unpacking a tuple:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Using Asterisk*
# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)


# =============================================================================
# Loop Tuples
# =============================================================================

# For Loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Using the range() and len() functions to print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


# =============================================================================
# Join Tuples
# =============================================================================

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)








































































    
    