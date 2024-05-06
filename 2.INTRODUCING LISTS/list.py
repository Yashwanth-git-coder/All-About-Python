"""
List:
    A list is a collection of items in a particular order. You can
    make a list that includes the letters of the alphabet, the
    digits from 0 to 9, or the names of all the people in your
    family. You can put anything you want into a list, and the
    items in your list don’t have to be related in any particular
    way. Because a list usually contains more than one element,
    it’s a good idea to make the name of your list plural, such as
    letters, digits, or names.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

"""

friends = ["john", "mick", "rock", "megan", "roll"]
print(friends)

# Accessing Elements in a List
print(friends[0])
print(friends[0].title())

# Using Individual Values from a List
print(f"My best friend name is : {friends[1].title()}")

# Modifying Elements in a List
motorcycle = ['honda', 'splender', 'suzuki']
print(motorcycle)

motorcycle[0] = 'ducati'
print(motorcycle)

# Adding Elements to a List
motorcycle.append('honda')
print(motorcycle)

# Inserting Elements into a List
motorcycle.insert(2, 'rollsroyce')
print(motorcycle)

# Removing Elements from a List
del motorcycle[1]
print(motorcycle)

poped_motorcycle = motorcycle.pop()
print(motorcycle)
print(poped_motorcycle)

motorcycle.remove('ducati')
print(motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Organizing a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the Original list :")
print(cars)

print("\nHere is the Sorted list :")
print(sorted(cars))

# Printing a List in Reverse Order
car = ['bmw', 'audi', 'toyota', 'subaru']
car.reverse()
print(f"\n{car}")

# Finding the Length of a List
print(len(cars))