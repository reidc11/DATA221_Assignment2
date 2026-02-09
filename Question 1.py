# Caitlin Reid | 30245427
# Question 1 (1 Point)
# In this question, you will practice reading a text file and performing basic text preprocessing before computing word
# statistics.
# Using sample-file.txt:
# • Read the file and split it into tokens (words).
# • Convert all tokens to lowercase.
# • Remove punctuation characters from the beginning and end of each token.
# • Keep only tokens that contain at least two alphabetic characters.
# • Count word frequencies and print the 10 most frequent words in descending order in the format: word -> count.

with open('sample-file.txt', 'r') as file:
    studentFileContents = file.read()
    fileWords = studentFileContents.lower().split()

cleanWords = []

for word in fileWords:
    cleaned = ""
    for character in word:
        if character.isalpha():
            cleaned += character
    if len(cleaned) >= 2:
        cleanWords.append(cleaned)

wordCounts = {}
for word in cleanWords:
    if word in wordCounts:
        wordCounts[word] += 1
    else:
        wordCounts[word] = 1

top10Words = sorted(wordCounts.items(), key = lambda item: item [1], reverse = True)[:10]

for word, count in top10Words:
    print(f" {word} -> {count}")


