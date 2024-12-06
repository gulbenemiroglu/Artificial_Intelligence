# =============================================================================
#       SETS
# =============================================================================
thisset = {"apple", "banana", "cherry"}
print(thisset)


# =============================================================================
# SETS ARE:
# 
# UNORDERED (unindexed)
# UNCHANGABLE (cannot change its items, but you can remove items and add new items)
# DUPLICATES NOT ALLOWED  (Sets cannot have two items with the same value.)
# =============================================================================


thisset = {"apple", "banana", "cherry", "apple"}
# Duplicate values will be ignored:
print(thisset)

# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}


# type()function:
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


# Access Items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

# Add Items - add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets - with update() method
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Add Any Iterable - with update() method
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# =============================================================================
# Remove Set Items
# =============================================================================

# use the remove(), or the discard() method. Remove a random item by using the pop() method
# If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry","mango"}
thisset.remove("banana")
thisset.remove("banana")
print(thisset)
thisset.discard("mango")
thisset.discard("mango")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

# FOR LOOP
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# =============================================================================
# Join Sets
# There are several ways to join two or more sets in Python. 
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates. 
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.
# =============================================================================


# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)

# Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

# Update
# The update() method inserts all items from one set into another.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


# Intersection
# Keep ONLY the duplicates

# The intersection() method will return a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)


# You can use the & operator instead of the intersection() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2 
print(set3)

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)


# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)   
#or you can use set3 = set1 - set2
# Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.
print(set3)

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# You can use the ^ operator instead of the symmetric_difference()


# The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)



























