# =============================================================================
#       LISTS
# =============================================================================

mylist = ["apple", "banana", "cherry"]
type(mylist)

# =============================================================================
# LISTS ARE:
# 
# ORDERED (indexed)
# CHANGABLE (change, add, and remove items)
# ALLOW DUPLICATES (lists can have items with the same value)
# =============================================================================


# =============================================================================
# List Length
# =============================================================================
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# =============================================================================
# List Items - Data Types
# =============================================================================
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))


# =============================================================================
# The list() Constructor
# =============================================================================

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# =============================================================================
# Access List Items
# =============================================================================
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
# =============================================================================
# Change List Items 
# =============================================================================
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)



# =============================================================================
# Add List Items
# =============================================================================


# Append Items:
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items:
# To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Extend List
# To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# =============================================================================
# Remove List Items
# =============================================================================

# If there are more than one item with the specified value, the remove() method removes the first occurrence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index - pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List - The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# =============================================================================
# Loop Lists
# =============================================================================

# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# =============================================================================
# List Comprehension 
# 
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. 
# =============================================================================
  
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)  
  
# you can do all that with only one line of code:  
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)  
  
# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
  
# Condition
# The condition is like a filter that only accepts the items that valuate to True.  
  
newlist = [x for x in fruits if x != "apple"] 
print(newlist)
  
# With no if statement:
newlist = [x for x in fruits]  
  
# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.

# Example
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]  
print(newlist)  
  
# Same example, but with a condition:
newlist = [x for x in range(10) if x < 5]  
print(newlist)  
 
# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# Example
# Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]
print(newlist)  

# You can set the outcome to whatever you like:
# Example
# Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]
print(newlist)


# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Example
# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


# =============================================================================
# Sort Lists
# =============================================================================

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

# Example
# Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# So if you want a case-insensitive sort function, use str.lower as a key function:
# Example
# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# =============================================================================
# Copy Lists
# =============================================================================
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# =============================================================================
# Join Lists
# =============================================================================

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Or you can use the extend() method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)



# =============================================================================
# 
#           List Methods
#
# =============================================================================
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# =============================================================================
