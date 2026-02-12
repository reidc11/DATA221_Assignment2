# Data 221 Assignment 2 Caitlin Reid | 30245427
# Question 9
# In this question, you will extract tabular data from a webpage and store it in a structured format.
# Scrape the Wikipedia page:
# https://en.wikipedia.org/wiki/Machine_learning
#   • Locate the first table inside the main content area (div with id mw-content-text) that contains at least 3 data rows.
#   • Extract the table header from <th> tags if present; otherwise create headers named col1, col2, col3, etc.
#   • Some rows may have fewer columns than others; pad missing values with empty strings.
#   • Save the extracted table to wiki_table.csv

# Sorry to whoever is marking this. I shouldn't have left this to last minute I've been fighting with this and I keep
# getting the worst output. I eventually asked chatgpt and its saying theres no regular data table in the article so its
# grabbing the navigation table.

import requests
from bs4 import BeautifulSoup
import csv
url = "https://en.wikipedia.org/wiki/Machine_learning"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content_div = soup.find("div", id="mw-content-text")

tables = content_div.find_all("table")
chosen_table = None

for table in tables:
    table_classes = table.get("class")

    if table_classes and "sidebar" in table_classes:
        continue

    rows = table.find_all("tr")
    data_row_count = 0
    for r in rows:
        if r.find_all("td"):
            data_row_count += 1

    if data_row_count >= 3:
        chosen_table = table
        break


all_rows = chosen_table.find_all("tr")

first_row_ths = all_rows[0].find_all("th")
headers_list = []

if first_row_ths:
    for th in first_row_ths:
        text = th.get_text(strip=True)
        headers_list.append(text)

data_rows = []

for tr in all_rows:
    if tr.find_all("td"):
        cells = tr.find_all(["th", "td"])
        row_values = [cell.get_text(strip=True) for cell in cells]
        data_rows.append(row_values)


max_cols = 0
for row in data_rows:
    if len(row) > max_cols:
        max_cols = len(row)

if not headers_list:
    headers_list = []
    for i in range(max_cols):
        headers_list.append("col" + str(i+1))

for row in data_rows:
    while len(row) < max_cols:
        row.append("")

with open("wiki_table.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers_list)
    writer.writerows(data_rows)



