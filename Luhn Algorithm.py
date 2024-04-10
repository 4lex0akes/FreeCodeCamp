def verify_card_number(card_number):
    sum_of_odd_digits = 0
    # The [::-1] creates a variable containing negative digits in a string.
    card_number_reversed = card_number[::-1]
    # The [::2] creates a variable containing every other digit of a string.
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        # The below is just variable in the 'for' loop.
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # The below [1::2] represents even digits only.
    even_digits = card_number_reversed[1::2]


    # The below "for 'x' in 'y':" respresemts a loop, in this case specifically for the even digits, then prints to console.
    for digit in even_digits:
        # The below 'int()' is used to represents a number (integer), in this case multiplited by 2.
        number = int(digit) * 2
        # The below "if 'x' >= 10:" is used to prevent multiplication of one digit from being greater than 9.
        if number >= 10:
            # The below is "number" being assigned to the result of "number // 10" (integer division) plus the modulus of "number" and "10".
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
        # I'm not sure why the above uses += as addition and the below uses +, but there seems to be a difference between the two, perhaps depending on context.
    total = sum_of_odd_digits + sum_of_even_digits
    # My first time encountering 'return' - used in the direction "Return the result of comparing '0' to 'total' modulo '10'".
    return 0 == total % 10        

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)

    # "if" and "else" Seem fairly straight forward, just apply an "if" followed by ":" onto your variable and make sure to provide an "else:" statement to follow, I think.
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()