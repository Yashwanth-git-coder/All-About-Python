from bs4 import BeautifulSoup
import requests


URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which Year do you want to Travel to. Type the date in this format YYYY-MM-DD: ")

response = requests.get(URL + date)
billboard = response.text


soup = BeautifulSoup(billboard, "html.parser")
songs = soup.select("li ul li h3")
song_lists = []
for bill_song in songs:
    song = bill_song.getText().strip()
    song_lists.append(song)

print(song_lists)