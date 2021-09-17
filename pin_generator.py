# Scrip to generate 4 integer random numbers
import random # Import random module

print("Pin Generator:")
print()

pin = [] # Generate an empty list

# Create our 4 random integer numbers
num_1 = random.randrange(0, 10)
num_2 = random.randrange(0, 10)
num_3 = random.randrange(0, 10)
num_4 = random.randrange(0, 10)

# Append the four random integer numbers to the empty list
pin.append(num_1)
pin.append(num_2)
pin.append(num_3)
pin.append(num_4)

# Print the list
print(pin)
