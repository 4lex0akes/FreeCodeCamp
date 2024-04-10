def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    # In the above statement, 'amount' is a string being used as a key, whilst amount is the value of the pair "'amount': amount" contained within {}. Pairs are seperated with a ",".

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
        # In the above statement, I have modified the f-string expression to access the value of the 'amount' key and the 'category' key in the expense dictionary.

# Below is a new function definition of "total_expenses" with the value of "expenses".
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    # The above lambda function uses "expense" as the paramater and returns the value of the "'amount'"" key in the 'expense' dictionary. 
    # The "return" command above should return the result of the "sum()" function.

# Below is a function defined as "filter_expenses_by_category", containing 2... Variables?
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    # Above is a plain lambda function, using "expense" as the parameter and returning the comparison between the value of the "'category'" key of the "expense" dictionary and "category".
    # It is also now being used in a "filter()" function which allows you to select items from an iterable, such as a list, based on the output of a function.
    # In my example above, I have called a "filter()" passing my lambda function as the first argument and the "expenses" list as the second argument.

# The below is a test variable with a lambda function value of "x * 2".
# -- test = lambda x: x * 2
# -- print(sum(map(test, [2, 3, 5, 8])))
# The above is a print call to print the lambda function with variable_name "test" using with "(3)" as the argument.
# It is also a "sum()" command with "map()" as the value.

def main():
    expenses = []
    # Below is my first encounter of a "while" loop. It runs a portion of code until a specified condition is "True".
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')
        # The above is an "input()" function that takes a user input and returns it in the form of a string.
        # In this "input()", the string "'Enter your choice: '" is the argument and it is the result of a variable names "choice".
        
        # Here, I have created an if statement to check if "choice" is equal to the string "'1'". If it is true, it will be the starting point for adding a new expense.
        # Inside this "if" statement body, I have declared a variable "amount" and assigned it an empty "input()" call.
        if choice == '1':
            amount = float(input('Enter amount: '))
            # Above is my first encounter of the "float" function, which takes a string (in this case, a string) or integer number as an argument and returns a floating point number.
            category = input('Enter category: ')
            # Next is a call to "add_expense" function to add the new expense to the "expenses" list with 3 arguments: "expenses, amount, category".
            add_expense(expenses, amount, category)
        # Below is an "elif" statement that only apply after an "if" statement. This "elif" statement checks if the user's choice equals the string "'2'" and then prints the string "'\nAll Expenses:'".
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
            # This new line above is a "print_expenses" call within the "elif" statement with "expenses_from_category" as the iterator to the call.        

        elif choice == '5':
            print('Exiting the program.')
            break
            # "break" is used to stop the execution of the "while" loop. (I think it must be placed within the final function)

# You can use the "__name__" variable to determine if a Python script is being run as the main program or if it is being imported as a module (code written in another Python file).
# Below is an "if" statement to check if "__name__" equals "__main__" with the "main()" call inside this block.
if __name__ == '__main__':
    main()
    # "main()" is a call to the original function containing the list [1-5].