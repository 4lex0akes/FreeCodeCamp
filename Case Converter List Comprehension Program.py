# In this project, I'm going to learn about list comprehensions in Python by building a program that can take a "camelCase" or "PascalCase" formatted string and convert that to a "snake_case" formatted string.
# List comprehensions in Python are a concise way to construct a list without using loops or the ".append()" method. Apart from being briefer, list comprehensions often run faster.

# Here I have defined a new function named "convert_to_snake_case" with a string name "pascal_or_camel_cased_string" as the input.
def convert_to_snake_case(pascal_or_camel_cased_string):
    # Below I've created a new list named "snake_cased_char_list" inside the function. Use "[]" to create the new list.
    snake_cased_char_list = []
    # Next I've added a "for" loop to iterate through "pascal_or_camel_cased_string" with the target variable "char".
    for char in pascal_or_camel_cased_string:
        # Below is my first encounter of the ".isupper()" string method to check for uppercase characters.
        if char.isupper():
            # Next, I've used the ".lower()" string method to convert uppercase to lowercase. I've then concatenated an underscore to the character using "+".
            # I've also assigned the charater to a variable named "converted_character" inside the statement body.
            converted_character = '_' + char.lower()
            # Now I'm using the ".append()" method to add the converted char to the list I created earlier. (The ".append()" method adds a given object to the end of the list you invoke it on.)
            snake_cased_char_list.append(converted_character)
        # Here I've added an "else:" clause to add characters that are already in lower case to the list of converted characters inside the body of the else clause.
        else:
            snake_cased_char_list.append(char)
    # Below is a ".join()" string method to convert the list of characters into a string.
    snake_cased_string = ''.join(snake_cased_char_list)
