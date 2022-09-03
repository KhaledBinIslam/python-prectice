# Variables that are created outside of a function are known as global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)