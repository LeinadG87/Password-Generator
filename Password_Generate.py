# Password generator
import random
import string

while True:
    try:
        user_input = input("Input a length for password between 0 to 50:")
        pass_len = int(user_input)
        if 0 < pass_len <= 50:
            break
        else:
            print("input needs to be between 0 & 50")
    except:
        print("Enter a number value")


# Define the characters you want to use for generating the random string
characters = string.ascii_letters + string.digits  # This includes letters (both upper and lower case) and digits

# Generate a random string of length 10
random_string = ''.join(random.choice(characters) for _ in range(int(pass_len)))

# Print the random string
print(random_string)
