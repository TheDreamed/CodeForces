import sys

counter = 0
lines = sys.stdin.read().strip().split('\n')

for line in lines[1:]:  # Skip the first line
    if '+' in line:
        counter += 1
    if '-' in line:
        counter -= 1

print(counter)
