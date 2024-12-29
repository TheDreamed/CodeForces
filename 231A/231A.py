import sys

counter = 0
lines = sys.stdin.read().strip().split('\n')
for line in lines[1:]:  # Skip the first line
    line = line.replace(" ", "")
    count = 0
    for i in range(len(line)):  
        if line[i] == '1':
            count += 1
    if count >= 2:
        counter += 1

print(counter)