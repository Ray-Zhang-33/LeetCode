import sys

for line in sys.stdin:
    if line.strip() == "0 0":
        sys.exit()
    data = list(map(int, line.strip().split()))
    result = data[0] + data[1]
    print(result)
