import sys

def cauculate_number_of_power_divisors(even_number):
    power_divisors = []
    for num in even_number:
        binary = bin(num)[2:]
        count = len(binary) - len(binary.rstrip('0'))
        power_divisors.append(count)
    return power_divisors

# Divide and preprocess even numbers 
def split_numbers(array):
    even = []
    odd = []
    for number in array:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    power_divisors = cauculate_number_of_power_divisors(even)
    sorted_even = [(n, pd) for n, pd in sorted(zip(even, power_divisors), reverse=True)]
    print(sorted_even, odd)
    return sorted_even, odd        

def caculate_number_of_operations():
    even, odd = split_numbers(array)
    operations = 0
    if len(odd) >= len(even):
        operations = len(even)
    else:
        operations += len(odd)
        even = even[len(odd):]
        for t in even:
            operations += t[1]
    print(operations)

# Read input from stdin
number_of_arrays = sys.stdin.readline().strip()
arrays = []
for _ in range(int(number_of_arrays)):
    size_of_array = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().strip().split()))
    # array = list(int(e) for e in sys.stdin.readline().strip().split())
    arrays.append(array)

# Call function to caculate number of operations
for array in arrays:
    caculate_number_of_operations()