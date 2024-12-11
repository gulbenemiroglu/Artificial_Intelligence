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