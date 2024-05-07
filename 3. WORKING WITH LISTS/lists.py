magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician} \n")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick! \n")

friends = ['John', 'david', 'mick']
for friend in friends:
    print(f"{friend.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {friend.title()}.\n")
print(f"Thank you, everyone. That was a great magic show!")

# Making Numerical Lists
# Using the range() Function
for value in range(1,5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

# Generating Even numbers from 1 to 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Generating Squares numbers using the range function
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

print(max(digits))

print(sum(digits))

# List Comprehensions
squares1 = [value**2 for value in range(1, 11)]
print(squares1)

family_members1 = ['aryan', 'abhi']
family_members = [member for member in family_members1]
print(family_members)

# Working with Part of a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

# Looping Through a Slice
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)