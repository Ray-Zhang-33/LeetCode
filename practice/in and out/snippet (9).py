import sys

for line in sys.stdin:
    data = list(line.strip().split(","))
    print(",".join(sorted(data, key=lambda x: x.lower()[0])))
