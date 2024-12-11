# =============================================================================
#       DICTIONARIES
# =============================================================================
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# =============================================================================
# DICTIONARIES ARE:
# 
# ORDERED (indexed)  
# !!!As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# CHANGABLE (we can change, add or remove items after the dictionary has been created.)
# DUPLICATES NOT ALLOWED  (Dictionaries cannot have two items with the same key)
# =============================================================================

# Dictionary Length - len()
print(len(thisdict))


# Dictionary Items - Data Types
# The values in dictionary items can be of any data type: String, int, boolean, and list data types

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


# =============================================================================
# The dict() Constructor
# =============================================================================

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# =============================================================================
# Accessing Items
# =============================================================================

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)


# =============================================================================
# Get Keys
# =============================================================================

x = thisdict.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change




# =============================================================================
# Get Values
# =============================================================================

x = car.values()
print(x)

# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


# =============================================================================
# Get Items
# =============================================================================

x = thisdict.items()
print(x)

# Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change



# =============================================================================
# Check if Key Exists - "in" Keyword
# =============================================================================

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# =============================================================================
# Change Values
# =============================================================================

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018


# =============================================================================
# Update Dictionary
# =============================================================================

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


# =============================================================================
# Adding Items
# =============================================================================

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


# =============================================================================
# Removing Items
# =============================================================================

# The pop() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists

# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)











































