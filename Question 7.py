# Data 221 Assignment 2 Caitlin Reid | 30245427
# Question 7
# In this question, you will work on extracting structured content from a webpage using Beautiful Soup.
# Scrape the Wikipedia page:
# https://en.wikipedia.org/wiki/Data_science
# Write a program using requests and BeautifulSoup that:
# • Extracts and prints the page title from the <title> tag.
# • Extracts the first paragraph from the main article content inside the div with id mw-content-text.
# • The paragraph must contain at least 50 characters (after stripping whitespace).

import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Data_science"


headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

page_title = soup.title.text
print(f"Title: {page_title}")


content_div = soup.find("div", id="mw-content-text")

paragraphs = content_div.find_all("p")

for text in paragraphs:
    paragraph_text = text.get_text(separator=" ", strip=True)
    if len(paragraph_text) >= 50:
        print("First paragraph: ")
        print(paragraph_text)
        break