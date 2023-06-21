# Imports
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import smtplib
import ssl
from email.message import EmailMessage

# Load environment variables
load_dotenv()



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
    try:
        article_id = article.get("id")
        article_class = article.find(class_="titleline")
        article_text = article_class.find("a").getText()
        article_link = article_class.find("a").get("href")
        article_class_score = soup.find(class_="score", id=f"score_{article_id}").getText()
        # append to lists
        article_texts.append(article_text)
        article_links.append(article_link)
        article_scores.append(int(article_class_score.split()[0]))  # split the score on whitespace and convert to int
    except AttributeError:
        pass

#  get index of highest score and sorted list of scores
scores_sorted = sorted(article_scores, reverse=True)
highest_score = max(article_scores)
highest_score_index = article_scores.index(highest_score)

# Build message from top 5 articles
email_message = ""
for i in range(0, 5):
    score_index = scores_sorted[i]
    article_index = article_scores.index(score_index)
    article_message = f"""{article_texts[article_index]}
{article_links[article_index]}
Upvotes: {article_scores[article_index]}

"""
    email_message += article_message

# Email constants
sender = os.getenv("sender")
password = os.getenv("senderPwd")
recipient = os.getenv("recipient")
smtp_server = "smtp.gmail.com"
smtp_port = 587
message = EmailMessage()
message.set_content(email_message)
context = ssl.create_default_context()
print(sender)
print(password)

# Send email
with smtplib.SMTP(smtp_server, smtp_port) as connection:
    connection.starttls(context=context)
    connection.login(user=sender, password=password)
    connection.sendmail(from_addr=sender, to_addrs=recipient, msg=f"Subject: Hacker News Top Stories\n\n{message}")







