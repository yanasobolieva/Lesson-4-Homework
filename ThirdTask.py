import random


# Create a function to sum digits
def sum_digits(some_int):
    sum_result = 0
    while some_int:
        sum_result += some_int % 10
        some_int //= 10
    return sum_result


# Generate random int
randomInt = random.randint(100, 999)
print(randomInt)

# Apply function to random int
print(sum_digits(randomInt))
