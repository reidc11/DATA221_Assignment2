# Data 221 Assignment 2 Caitlin Reid | 30245427
# Question 3
# In this task, you will identify lines that are nearly identical after basic normalization.
# Two lines are considered near-duplicates if they become identical after converting to lowercase and removing all
# whitespace and punctuation characters.
# Using sample-file.txt:
# • Identify sets of near-duplicate lines.
# • Print the number of such sets.
# • Print the first two sets you find, including line numbers and original lines.

with open ('sample-file.txt', 'r') as file:
    lines = file.readlines()

seen = {}


line_num = 1

for line in lines:
    normalized = ''.join(line.lower().split())
    original_line = line.strip()

    if normalized in seen:
        duplicates.append((seen[normalized], line_num))
    else:
        seen[normalized] = line_num

    line_num += 1

num_sets = 0

for normalized_line in seen:
    if seen[normalized_line] > 1:
        num_sets += 1

print(f'Number of duplicate sets: {num_sets}')

print('Set 1')
print(f'Line{line_num}: {line_text}')

print('Set 2')
print(f'Line{line_num}: {line_text}')