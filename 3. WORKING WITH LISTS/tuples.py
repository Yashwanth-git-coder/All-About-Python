"""

A tuple looks just like a list, except you use parentheses
 instead of square brackets. Once you define a tuple, you can
 access individual elements by using each item’s index, just
 as you would for a list.
 For example, if we have a rectangle that should always be
 a certain size, we can ensure that its size doesn’t change by
 putting the dimensions into a tuple:

"""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# You can loop over all the values in a tuple using a for loop, just as you did with a list:

# Writing Over a Tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


"""

 When compared with lists, tuples are simple data
 structures. Use them when you want to store a set of values
that should not be changed throughout the life of a
 program.

"""

