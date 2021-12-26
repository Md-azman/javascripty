print("hello,world")

if 5 > 7:
    print("five is greater than two")
else:
    print("five is less than two")
    

x = 5
y = "hello azman"
print(x,y)     

# this is a comment in python

#variables

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

#assign mutiple values in variables:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables :

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
#If you have a collection of values in a list, tuple etc.
#Python allows you extract the values into variables. This is called unpacking.

fruits = ["app", "ban", "cher"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output variables :

a = "azman"
print("mohamed "+ a)

A = "mohamed"
B = "azman"
print("my name is "+ A,B)


#create varibles outside of the func and use inside of the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#globle keywprd

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


