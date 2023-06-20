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
articles = soup.find_all(class_="athing")

article_texts = []
article_links = []
article_scores = []

for article in articles:
    article_id = article.get("id")
    article_class = article.find(class_="titleline")
    article_text = article_class.find("a").getText()
    article_link = article_class.find("a").get("href")
    article_class_score = soup.find(class_="score", id=f"score_{article_id}").getText()
    # append to lists
    article_texts.append(article_text)
    article_links.append(article_link)
    article_scores.append(int(article_class_score.split()[0]))  # split the score on whitespace and convert to int

#  get index of highest score
highest_score = max(article_scores)
highest_score_index = article_scores.index(highest_score)

# print article with the highest score
print(f"""Article with the highest score:
{article_texts[highest_score_index]}
{article_links[highest_score_index]}
Upvotes: {article_scores[highest_score_index]}""")





