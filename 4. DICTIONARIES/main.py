"""
 Working with Dictionaries
"""

alien_0 = {'color': 'green', 'points': 5}

"""
 Accessing Values in a Dictionary
"""

print(alien_0['color'])

new_points = alien_0['points']
print(f"You just earned {new_points} points !")

"""
 Adding New Key-Value Pairs
"""

print(alien_0)

alien_0['x_position'] = 23
alien_0['y_position'] = 43

print(alien_0)

"""
Starting with an Empty Dictionary
"""

alien_1 = {}

alien_1['color'] = 'Red'
alien_1['points'] = 50
alien_1['x_position'] = 23
alien_1['y_position'] = 43

print(alien_1)

"""
Modifying Values in a Dictionary
"""

print(f"The Alien1 is {alien_1['color']}.")

alien_1['color'] = 'Yellow'
print(f"The alien1 is now {alien_1['color']}.")

alien_1['speed'] = 'medium'
print(alien_1)

print(f"Original position : {alien_1['x_position']}.")

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"New position: {alien_1['x_position']}.")

"""
 Removing Key-Value Pairs
"""

del alien_1['points']
print(alien_1)

"""
 A Dictionary of Similar Objects
"""

favorite_languages = {
    'jen': 'Python',
    'sarah': 'rust',
    'edward': 'c',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

"""
 Using get() to Access Values
"""


