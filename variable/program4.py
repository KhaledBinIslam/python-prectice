# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.
# This is called unpacking.

vegetables = ["potato", "tomato", "onion"]
x, y, z = vegetables
print(x, y, z)

# in print() we can output multiple variables separated by comma

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# In the print() function, when you try to combine a string and a number with the + operator,
# Python will give you an error:
