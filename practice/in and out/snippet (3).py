import sys

for line in sys.stdin:
    if line.strip() == "0":
        sys.exit()
    data = list(map(int, line.strip().split()))
    result = sum(data) - data[0]
    print(result)
