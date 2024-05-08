from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

"""
achore_tags = soup.find_all(name="a")
print(achore_tags)
"""
article_tag = soup.find(name="span", class_="titleline")
print(article_tag.getText())
print(article_tag.get("href"))




