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