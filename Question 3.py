# Data 221 Assignment 2 Caitlin Reid | 30245427
# Question 3
# In this task, you will identify lines that are nearly identical after basic normalization.
# Two lines are considered near-duplicates if they become identical after converting to lowercase and removing all
# whitespace and punctuation characters.
# Using sample-file.txt:
# • Identify sets of near-duplicate lines.
# • Print the number of such sets.
# • Print the first two sets you find, including line numbers and original lines.

import string

with open('sample-file.txt', 'r') as file:
    lines = file.read().splitlines()


line_groups = {}

line_num = 1

for line in lines:

    if line.strip() == "":
        line_num += 1
        continue

    lower_line = line.lower()

    normalized_line = ""
    for character in lower_line:
        if (character not in string.whitespace) and (character not in string.punctuation):
            normalized_line += character

    original_line = line.strip()

    if normalized_line in line_groups:
        line_groups[normalized_line].append((line_num, original_line))
    else:
        line_groups[normalized_line] = [(line_num, original_line)]

    line_num += 1

duplicate_sets = []

for key in line_groups:
    if len(line_groups[key]) > 1:
        duplicate_sets.append(line_groups[key])

print(f'Number of duplicate sets: {len(duplicate_sets)}')


if len(duplicate_sets) >= 1:
    print('\nSet 1')
    for line_info in duplicate_sets[0]:
        print(f'Line {line_info[0]}: {line_info[1]}')

if len(duplicate_sets) >= 2:
    print('\nSet 2')
    for line_info in duplicate_sets[1]:
        print(f'Line {line_info[0]}: {line_info[1]}')
