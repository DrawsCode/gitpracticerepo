import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Check if the number is even or odd
if random_number % 2 == 0:
    print(f"The number {random_number} is even.")
else:
    print(f"The number {random_number} is odd.")
