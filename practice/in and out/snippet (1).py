import sys

input = sys.stdin.readlines()
number_of_data = int(input[0])
for l in input[1:]:
    data = list(map(int, l.strip().split()))
    result = data[0] + data[1]
    print(result)