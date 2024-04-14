# A Python module is a file containing code designed to perform specific tasks. The Python standard library contains many modules that you can import and use in your code. You can achieve this by using the import statement followed by the name of the module.
# In this project, I am going to use different constants from the string module.
# You can access the utilities defined inside the imported module through the dot notation. The dot notation works by appending a dot followed by the utility name to the module name. For example, here's how to access the "ascii_lowercase" constant:
# It is a common convention to place import statements at the top of your code. And additionally, in case of multiple import statements, sort them in alphabetical order to improve readability.

# The algorithm on which "random" relies makes the generated pseudo-random numbers predictable. Therefore, although the random module is suitable for the most common applications, it cannot be used for cryptographic purposes, due to its deterministic nature.
import random

import secrets
import string

def generate_password(length):
# Define the possible characters for the password.
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Next I will declare a variable named "all_characters" and assign it the result of concatenating my existing variables.
    all_characters = letters + digits + symbols
    # For future reference, "''" represents an empty string. (Being assigned to the "password" variable in this example)
    password = ''

    # Next, I've written a "for" loop with "i" as the loop variable, using the "range()" function to iterate up to the value of the "length".
    # Inside the loop, I've used the addition assignment operated to add a random charater from "all_characters" to the current value of "password". 
    # I've used the "choice()" function from the "secrets" module for that.
    for i in range(length):
        password += secrets.choice(all_characters)

    return password

##########################
# - print(all_characters)
    # "Call the "random()" function from the "random" module and print the result."
# - print(random.random())
    # The "choice()"" function from the random module takes a sequence and returns a random item of the sequence.
# - print(secrets.choice(all_characters))
##########################