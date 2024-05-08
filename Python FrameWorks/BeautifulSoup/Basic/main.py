from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

"""

print(soup.title)
print(soup.title.name)
print(soup.title.string)

"""

all_of_the_anchor_tag = soup.find_all(name="a")

"""

print(f"{all_of_the_anchor_tag} \n")

for tag in all_of_the_anchor_tag:
    print(tag.getText())
    print(tag.get("href"))

"""

heading = soup.find(name="h1", id="name")

"""

print(heading.string)

"""


section_heading = soup.find(name="h3", class_="heading")

"""

print(section_heading.string)
# or
print(section_heading.getText())
# or
print(section_headind.get("class"))

"""

name = soup.select_one("#name")
print(name)

heading = soup.select(".heading")
print(heading)

