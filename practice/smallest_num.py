import sys

# -------------- Main ---------------
# Read input from stdin
given_input = sys.stdin.readline().strip()
# Check if given number is empty or 1 or not a digit
if given_input == '' or not given_input.isdigit() or int(given_input) > 45:
    sys.stdout.write("-1")
    sys.exit()
elif int(given_input) < 9:
    sys.stdout.write(given_input)
    sys.exit()

number = int(given_input)
digits = []
for i in range(9, -1, -1):
    if number >= i:
        digits.append(i)
        number -= i
digits.sort()

if number != 0:
    digits.insert(0, number)
    smallest_number = int(''.join(map(str, digits)))
else:
    smallest_number = int(''.join(map(str, digits)))
sys.stdout.write(str(smallest_number))