# Imports
from bs4 import BeautifulSoup
import requests

# #  Open HTML file
# with open('website.html', encoding='utf-8') as html_file:  # encoding='utf-8' is used to avoid UnicodeDecode errors
#     content = html_file.read()
#
# # Parse HTML file
# soup = BeautifulSoup(content, 'html.parser')
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

# Scrape Hacker News
requests = requests.get("https://news.ycombinator.com/news")
yc_webpage = requests.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article = soup.find(class_="athing", id="36380711")
article_class = article.find(class_="titleline")
article_text = article_class.find("a").getText()
article_link = article_class.find("a").get("href")
article_class_score = soup.find(class_="score", id="score_36380711").getText()

print(article_text)
print(article_link)
print(article_class_score)
