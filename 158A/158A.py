import sys

lines = sys.stdin.read().strip().split('\n')

# Parse the first line
n, k = map(int, lines[0].split())

# Parse the second line and convert to integers
scores = list(map(int, lines[1].split()))

# Get the k-th score (1-indexed, so k-1 for 0-indexed list)
threshold = scores[k-1]

# Count scores greater than or equal to the k-th score
counter = sum(1 for score in scores if score >= threshold)

print(counter)
