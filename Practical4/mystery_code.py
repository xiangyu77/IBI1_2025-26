# Answer: This script repeatedly asks the user for a number and prints its double.
#        It stops when the user enters 'stop'.

while True:
    user_input = input("Enter a number (or 'stop' to quit): ")
    if user_input == 'stop':
        break
    number = float(user_input)
    print("Double is:", number * 2)

