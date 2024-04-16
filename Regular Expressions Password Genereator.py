# A Python module is a file containing code designed to perform specific tasks. The Python standard library contains many modules that you can import and use in your code. You can achieve this by using the import statement followed by the name of the module.
# In this project, I am going to use different constants from the string module.
# You can access the utilities defined inside the imported module through the dot notation. The dot notation works by appending a dot followed by the utility name to the module name. For example, here's how to access the "ascii_lowercase" constant:
# It is a common convention to place import statements at the top of your code. And additionally, in case of multiple import statements, sort them in alphabetical order to improve readability.

# The algorithm on which "random" relies makes the generated pseudo-random numbers predictable. Therefore, although the random module is suitable for the most common applications, it cannot be used for cryptographic purposes, due to its deterministic nature.
import random

# The "re" module allows you to use regular expressions in your code.
import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
# Define the possible characters for the password.
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Next I will declare a variable named "all_characters" and assign it the result of concatenating my existing variables.
    all_characters = letters + digits + symbols
    
    while True:
        # For future reference, "''" represents an empty string. (Being assigned to the "password" variable in this example)
        password = ''

        # Next, I've written a "for" loop with "i" as the loop variable, using the "range()" function to iterate up to the value of the "length".
        # Inside the loop, I've used the addition assignment operated to add a random charater from "all_characters" to the current value of "password". 
        # I've used the "choice()" function from the "secrets" module for that.
        # A standalone single underscore is used to represent a value you don't care or that won't be used in your code. Your iteration variable is not actually used. I have modified the previous "i" variable into a single underscore.
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        # Here I have created a "constraints" variable and assigned it an empty list with "[]"
        # A tuple is another built-in data structure in Python. Tuples are very much like lists, but they are defined with parentheses (), instead of square brackets.
        # I've now modified the "constraints" list assignment by adding a tuple to my list, using "nums" as the first item and an empty string as the second item.
        # The character class "\d" is a shorthand for "[0-9]". Below I've replaced "[0-9]" with this short hand inside the first constraint.
        # In a character class, you can combine multiple ranges by writing one range after another inside the square brackets (without any additional characters). For example: [a-d3-6] is the combination of [a-d] and [3-6].
        # In the same way the [0-9] class is equivalent to \d, the [^0-9] class is equivalent to \D. Alphanumeric characters can be matched with \w and non-alphanumeric characters can be matched with \W.
        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]')
            # Below I have combined my raw string with an f-string and iterpolated my "symbols" variable within the f-string, using curly brackets "{}".
            (special_chars, fr'[{symbols}]')
        ]


        # Next, I've written a "for" loop to iterate over the "constraints" list. Using "constraint" and "pattern" as the loop variables.
        for constraint, pattern in constraints:
            # Inside the for loop, I've called the "findall()" function, passing "pattern" and "password" as the arguments.
            # I've also passed my existing "findall()" function call to the "len()" function.
            len.re.findall(pattern, password)


        # I believe I must "return" the value to close the for loop.
        return password
    
# A regular expression, or regex, is a pattern used to match a specific combination of characters inside a string. It is a valid alternative to if/else conditional statements when you need to match or find patterns inside a string for validation purposes, character replacement, and others.
# The "compile()" function from the re module compiles the string passed as the argument into a regular expression object that can be used by other re methods.
# The "search()" function from the re module analyzes the string passed as the argument looking for the first place where the regex pattern matches the string.    
# In your pattern, you can add a quantifier after a character to specify how many times that character should be repeated. For example, the "+" quantifier means it should repeat one or more times.
# - "pattern = re.compile('l+')"
# You can obtain the same result without using the "compile()" function. Here, I have removed the previous above line of code and replaced it with the new shorter version by modifying my "pattern" variable into the literal string "'l+'" and changed the print call accordingly.
# - "pattern = 'l+'"
# A character class is indicated by square brackets and matches one character among those specified between the brackets. For example, "ma[dnt]" matchers iether "mad, man or mat".
# - "pattern = '[w[ha]]'"
# The caret, "^" placed at the beginning of the character class, matches all the characters except those specified in the class.
# - "pattern = '[^a-z]t'"
# The dot character is a wildcard that matches any character in a string. Except for a newline character by default.
# Here I have modified the "pattern" variable to match the entire string by replacing the current pattern with a "." followed by the "+".
# - "pattern = '.+'"
# If you need to match a character that has a special meaning in the pattern such as "." or "+", you can escape it by prepending a backslash character, "\". For example, this matches a literal plus sign: "\+".
# Python provides a particular type of string called raw string. Raw strings are prefixed with a "r". The key distinction from regular strings lies in how they handle the backslash character: in raw strings, backslashes are treated as literal characters rather than escape characters. When writing regular expressions, using raw strings is a good practice, since they can usually contain a lot of "\" characters.
pattern = r'\W'
quote = '_'

# To check that the generated password meets the required features, you are going to use the "findall()" function from the re module. It's similar to search but it returns a list with all the occurrences of the matched pattern.
# - "print(re.findall(pattern, quote))"

# - "new_password = generate_password(8)"
# - "print(new_password)"

##########################
# - print(all_characters)
    # "Call the "random()" function from the "random" module and print the result."
# - print(random.random())
    # The "choice()"" function from the random module takes a sequence and returns a random item of the sequence.
# - print(secrets.choice(all_characters))
##########################