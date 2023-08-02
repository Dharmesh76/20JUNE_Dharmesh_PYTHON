import random

def read_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        if lines:
            random_line = random.choice(lines)
            return random_line
        else:
            return "File is empty"

# Replace 'your_file.txt' with the actual file name
filename = 'your_file.txt'
random_line = read_random_line(filename)

print("Random Line:", random_line.strip())  # Remove newline character if present
