"""
Strings:
     A string is a series of characters. Anything inside quotes is
     considered a string in Python, and you can use single or
     double quotes around your strings like this:

     "This is a string."
     'This is also a string.'


"""

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "Yashwanth"
last_name = "S"
full_name = f"{first_name} {last_name}"
print(full_name)

# strip
favorite_lang = 'python'
print(favorite_lang.rstrip())

# Removing Prefixes
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

