import random

seed_value = 42  # You can use any integer value as the seed

random.seed(seed_value)  # Set the seed

# Now generate random numbers
random_integer = random.randint(1, 100)
random_float = random.uniform(0.0, 1.0)
random_element = random.choice([1, 2, 3, 4, 5])

print("Random Integer:", random_integer)
print("Random Float:", random_float)
print("Random Element:", random_element)
