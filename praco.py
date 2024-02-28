#Assigning multiple values to multiple variables
a,b,c = 5,3.2,"Hello"
print (a)
print (b)
print (c)
#Assigning same value to multiple variables at once.
x = y = "power learn project"
print(x)
print(y)
#unpack a collection/extract the values into variables.
Fruits = ["apple","banana","cherry"]
x,y,z = Fruits
print(x)
print(y)
print(z)
#output multiple variables seperated by commas
x = "Python"
y = "is"
z = "awesome"
print (x,y,z)
# plus (+) character works as a mathematical operator
x = 5
y = 10
print (x+y)
# [Strings are Arrays] get character at position 1
a = "Hello, World!"
print (a[1])
#string length
a = "Hello World!"
print (len(a))
#To check string
txt = "The best things in the world are free!"
print ("free"in txt)
txt = "The best things in the world are expensive!"
print ("free"in txt)
txt = "The best things in life are free"
print ("expensive"not in txt)
#python slicing strings.
b = "Hello, World!"
print (b[2:5])
#slice from start 
b = "Hello, World!"
print (b [:5])
#slice from the end
b = "Hello, World!"
print (b[2:])
#Negative indexing
b = "Hello, World!"
print (b[-5:-2])
#upper case
a = "Hello, World!"
print (a.upper())
#lower case
a = "HELLO, WORLD!"
print (a.lower())
#Remove whitespace
a = "Hello, World!"
print (a.strip())
#Replace string
a = "Hello, World!"
print (a.replace("H","J"))
#Split string
a = "Hello, World!"
print(a.split(","))
#String concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
#To add a space between them add a ""
a = "Hello"
b = "World"
c = a+""+b
print(c)
