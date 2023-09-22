# Password generator
import random
import string

# Define the characters you want to use for generating the random string
characters = string.ascii_letters + string.digits  # This includes letters (both upper and lower case) and digits

# Generate a random string of length 10
random_string = ''.join(random.choice(characters) for _ in range(10))

# Print the random string
print(random_string)
