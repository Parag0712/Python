# Type Casting is the method to convert the Python variable datatype into a certain data type in order to perform the required operation by users. In this article, we will see the various techniques for typecasting. There can be two types of Type Casting in Python:

# Python Implicit Type Conversion
# Python Explicit Type Conversion


a = 7

# Python automatically converts 
# b to float 

b = 3.0
print(type(b)) 

c = a + b 
print(c) 
print(type(c))

# Python automatically converts 
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))
a="1"
b="2"
d="parag"

c = int(a)+ int(b)
print(c)