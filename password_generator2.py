#Password_generator2

import random
import string

def generate_password(length):
    """Generate a random password of given length"""
    # Define the character set to be used for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices() to generate a list of characters
    password = ''.join(random.choices(characters, k=length))
    
    return password

# Example usage: Generate a password of length 10
password = generate_password(10)
print(password)
