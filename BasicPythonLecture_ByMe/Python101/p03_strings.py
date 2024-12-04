# ==================================
#         PYTHON STRINGS
# ==================================

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# ==================================
#         SLICING STRINGS
# ==================================

b = "Hello, World!"
print(b[2:5])       #llo

print(b[:5])        #Hello

print(b[2:])        #llo, World!"

print(b[-5:-2])     #orl"


# ==================================
#         MODIFY STRINGS
# ==================================

a = "Hello, World!"

# upper method
print(a.upper())

# lower method
print(a.lower())

# strip() method
# Whitespace is the space before and/or after the actual text, 
# and very often you want to remove this space.

a = "  Hello, World!   "
print(a.strip())          # returns "Hello, World!"

a = "*****Hello, World!****"
print(a.strip("*"))       # returns "Hello, World!"


# replace method
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# split() method
# The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(","))    # returns ['Hello', ' World!']


# ==================================
#         STRING CONCATENATION
# ==================================

#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# ==================================
#         STRING FORMAT
# ==================================

# We cannot combine strings and numbers like this:

age = 36
txt = "My name is John, I am " + age
print(txt)   #TypeError: can only concatenate str (not "int") to str

# But we can combine strings and numbers by using f-strings or the format() method!

#Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#A placeholder can include a modifier to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
    
#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)   #The price is 59.00 dollars

#A placeholder can contain Python code, like math operations:
txt = f"The price is {20 * 59} dollars"   
print(txt)    #The price is 1180 dollars




# ==================================
#         ESCAPE CHARACTERS
# ==================================

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.

# You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."

# To fix this problem, use the escape character \":

txt = "We are the so-called \"Vikings\" from the north."

# =============================================================================
# \'	    Single Quote	
# \\	    Backslash	
# \n	    New Line	
# \r	    Carriage Return	
# \t	    Tab	
# \b	    Backspace	
# \f	    Form Feed	
# \ooo	Octal value	
# \xhh	Hex value
# =============================================================================


# ==================================
#         STRING METHODS
# ==================================

# =============================================================================
# Method            Description
# capitalize()	    Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()	        Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()      Sets the tab size of the string
# find()	        Searches the string for a specified value and returns the position of where it was found
# format()	        Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()	        Searches the string for a specified value and returns the position of where it was found
# isalnum()	        Returns True if all characters in the string are alphanumeric
# isalpha()	        Returns True if all characters in the string are in the alphabet
# isascii()	        Returns True if all characters in the string are ascii characters
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit()	        Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	        Returns True if all characters in the string are lower case
# isnumeric()	    Returns True if all characters in the string are numeric
# isprintable()	    Returns True if all characters in the string are printable
# isspace()	        Returns True if all characters in the string are whitespaces
# istitle()	        Returns True if the string follows the rules of a title
# isupper()	        Returns True if all characters in the string are upper case
# join()	        Joins the elements of an iterable to the end of the string
# ljust()	        Returns a left justified version of the string
# lower()	        Converts a string into lower case
# lstrip()	        Returns a left trim version of the string
# maketrans()	    Returns a translation table to be used in translations
# partition()	    Returns a tuple where the string is parted into three parts
# replace()	        Returns a string where a specified value is replaced with a specified value
# rfind()       	Searches the string for a specified value and returns the last position of where it was found
# rindex()      	Searches the string for a specified value and returns the last position of where it was found
# rjust()       	Returns a right justified version of the string
# rpartition()  	Returns a tuple where the string is parted into three parts
# rsplit()	        Splits the string at the specified separator, and returns a list
# rstrip()      	Returns a right trim version of the string
# split()       	Splits the string at the specified separator, and returns a list
# splitlines()  	Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()       	Returns a trimmed version of the string
# swapcase()    	Swaps cases, lower case becomes upper case and vice versa
# title()       	Converts the first character of each word to upper case
# translate()   	Returns a translated string
# upper()	        Converts a string into upper case
# zfill()	        Fills the string with a specified number of 0 values at the beginning
# =============================================================================







