# Data 221 Assignment 2 Caitlin Reid | 30245427
# Question 8
# This task focuses on extracting structured heading information from a webpage.
# Using the same Wikipedia page https://en.wikipedia.org/wiki/Data_science
    # • Extract all <h2> section headings from the main content area (div with id mw-content-
    # text).
    # • Do not include headings containing the words: References, External links, See also, or
    # Notes.
    # • Remove any [edit] text from headings.
    # • Save the headings to headings.txt, one per line, in order.

import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Data_science"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content_div = soup.find("div", id="mw-content-text")

h2_tags = content_div.find_all("h2")

headings = []

for tag in h2_tags:
    text = tag.get_text(strip=True)
    headings.append(text)

cleaned_headings = []

exclude_words = ["References", "External links", "See also", "Notes"]

for tag in h2_tags:
    text = tag.get_text(strip=True)
    text = text.replace("[edit]", "")

    if not any(word in text for word in exclude_words):
        cleaned_headings.append(text)

with open("headings.txt", "w") as file:
    for heading in cleaned_headings:
        file.write(heading + "\n")



