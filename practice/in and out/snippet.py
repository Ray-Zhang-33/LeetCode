import sys

for line in sys.stdin:
    data = list(map(int, line.split()))
    result = data[0] + data[1]
    print(result)