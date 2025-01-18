import sys

input = sys.stdin.readlines()
number_of_data = int(input[0])
for l in input[1:]:
    data = list(l.strip().split())
    print(" ".join(sorted(data, key=lambda x: x.lower()[0])))