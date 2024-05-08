import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_movies = response.text

soup = BeautifulSoup(empire_movies, "lxml")
all_movies = soup.find_all(name="h3", class_="title")

movies_name = [movies_list.getText() for movies_list in all_movies]

# for movies_list in all_movies:
#     text = movies_list.getText()
#     movies_name.append(text)

movies = movies_name[::-1]

with open("movies_txt", mode="w",  encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")

print(f"{movies}\n")




