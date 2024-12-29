import sys

lines = sys.stdin.read().strip().split('\n')
for line in lines[1:]:  # Skip the first line
    length = len(line)
    if length > 10:
        print(line[0] + str(length - 2) + line[-1])  # Abbreviation logic
    else:
        print(line)
