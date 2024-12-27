import sys

with open(sys.argv[1], 'r') as file:
    for line in file:
        line = int(line.strip())
        if line % 2 == 0:
            print("YES")
        else:
            print("NO")
