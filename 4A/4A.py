import sys

for line in sys.stdin:
    line = int(line.strip())  # Convert each line to an integer
    if line % 2 == 0 and line > 2:
        print("YES")
    else:
        print("NO")
