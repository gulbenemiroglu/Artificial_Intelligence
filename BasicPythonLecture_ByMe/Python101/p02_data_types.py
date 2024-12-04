# =====================
#  DATA TYPES
# =====================

x = "Hello World"	#str
print(type(x))	

x = 20	#int	
print(type(x))	

x = 20.5	#float
print(type(x))	
	
x = 1j	#complex	
print(type(x))	

x = ["apple", "banana", "cherry"]	#list	
print(type(x))	

x = ("apple", "banana", "cherry")	#tuple	
print(type(x))	

x = range(6)	#range	
print(type(x))	

x = {"name" : "John", "age" : 36}	#dict	
print(type(x))	

x = {"apple", "banana", "cherry"}	#set	
print(type(x))	

x = frozenset({"apple", "banana", "cherry"})	#frozenset	
print(type(x))	

x = True	#bool	
print(type(x))	

x = b"Hello"	#bytes	
print(type(x))	

x = bytearray(5)	#bytearray	
print(type(x))	

x = memoryview(bytes(5))	#memoryview	
print(type(x))	

x = None	#NoneType
print(type(x))	


# =====================
#    TYPE CONVERSION
# =====================

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# =====================
#       CASTING
# =====================

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'



















