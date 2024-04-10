# A Python module is a file containing code designed to perform specific tasks. The Python standard library contains many modules that you can import and use in your code. You can achieve this by using the import statement followed by the name of the module.
# In this project, I am going to use different constants from the string module.
# You can access the utilities defined inside the imported module through the dot notation. The dot notation works by appending a dot followed by the utility name to the module name. For example, here's how to access the "ascii_lowercase" constant:
# It is a common convention to place import statements at the top of your code. And additionally, in case of multiple import statements, sort them in alphabetical order to improve readability.

import random
import string

# Define the possible characters for the password.
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Next I will declare a variable named "all_characters" and assign it the result of concatenating my existing variables.
all_characters = letters + digits + symbols
print(all_characters)
# "Call the "random()" function from the "random" module and print the result."
print(random.random())
# The "choice()"" function from the random module takes a sequence and returns a random item of the sequence.
print(random.choice(all_characters))