# Data 221 Assignment 2 Caitlin Reid | 30245427
# Question 10
# This final question asks you to design a reusable function for searching within text files.
# Write a function:
# def find_lines_containing(filename, keyword):
    # """
    # Returns a list of (line_number, line_text) for lines that contain ←↩
    # keyword
    # (case-insensitive). Line numbers start at 1.
    # """
# Test the function using sample-file.txt with keyword lorem.
#     • Print how many matching lines were found.
#     • Print the first 3 matching lines (line number and text).

def find_lines_containing(filename, keyword):
    matches = []

    with open(filename, "r") as file:
        line_number = 1
        for line in file:
            if keyword.lower() in line.lower():
                matches.append((line_number, line.strip()))
            line_number += 1

    return matches

results = find_lines_containing("sample-file.txt", "lorem")

print("Number of matching lines:", len(results))

print("First 3 matching lines:")
for match in results[:3]:
    print(match)