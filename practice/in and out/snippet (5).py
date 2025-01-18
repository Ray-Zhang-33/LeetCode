import sys

for line in sys.stdin:
    data = list(map(int, line.strip().split()))
    result = sum(data) - data[0]
    print(result)