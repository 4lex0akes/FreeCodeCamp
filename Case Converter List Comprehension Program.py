# In this project, I'm going to learn about list comprehensions in Python by building a program that can take a "camelCase" or "PascalCase" formatted string and convert that to a "snake_case" formatted string.
# List comprehensions in Python are a concise way to construct a list without using loops or the ".append()" method. Apart from being briefer, list comprehensions often run faster.

# Here I have defined a new function named "convert_to_snake_case" with a string name "pascal_or_camel_cased_string" as the input.
def convert_to_snake_case(pascal_or_camel_cased_string):
    # Below I've created a new list named "snake_cased_char_list" inside the function. Use "[]" to create the new list.
    snake_cased_char_list = []
    # Next I've added a "for" loop to iterate through "pascal_or_camel_cased_string" with the target variable "char".
    
##############################################################################    
    
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
    # I can also use the ".strip()" string method, using "'_'" as the argument in the example below, to strip such unwanted charaters.
    clean_snake_cased_string = snake_cased_string.strip('_')
    
    return clean_snake_cased_string

##############################################################################

    # These three lines of code do the same task as the for loop you worked on previously while being cleaner and somewhat faster.
    # When you start a list comprehension with an if statement like this, Python requires you to also add an else clause to the expression.
    # Python will interpret this updated expression as "append '_' + char.lower() to the list if char is in uppercase, append char as is otherwise" and this covers the case for both the capital and lowercase letters in the input string.
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    # This single line of code will join the list of characters into a string, strip off any dangling underscores, and return the resulting string. Add this line on the same level as the snake_cased_char_list variable and inside the convert_to_snake_case() function.
    return ''.join(snake_cased_char_list).strip('_')

##############################################################################

def main():
    print(convert_to_snake_case('SubjectTextToConvertHere'))

# Before running the below "main()" function, I'll need to make sure the file is running as a script, using the if statement below to check whether "__name__ == '__main__'".
if __name__ == '__main__':
    main()