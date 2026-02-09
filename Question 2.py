# Data 221 Assignment 2 Caitlin Reid | 30245427
#Question 2
# In this question, you will analyze pairs of consecutive words (called bigrams) from a text file.
# Using sample-file.txt:
# • Read the file and split it into tokens (words).
# • Convert all tokens to lowercase.
# • Remove punctuation characters from the beginning and end of each token.
# • Keep only tokens that contain at least two alphabetic characters.
# • Construct bigrams (pairs of consecutive cleaned words).
# • Count the frequency of each bigram.
# • Print the 5 most frequent bigrams in descending order in the format: word1 word2 -> count.

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

bigrams = []
for i in range (len(cleanWords)-1):
    bigram = cleanWords [i] + " " + cleanWords[i+1]
    bigrams.append(bigram)

bigramCounts = {}

for word in bigrams:
    if word in bigramCounts:
        bigramCounts[word] +=1
    else:
        bigramCounts[word] = 1
sortedBigrams = sorted(bigramCounts.items(), key = lambda x: x[1], reverse=True)

for word, count in sortedBigrams[:5]:
    print (f"{word} -> {count}")