"""
Write a Python program that takes two integer inputs from the user and calculates the value of 
the first number multiplied with the second. The program should perform the following tasks:
After printing "This program multiplies two numbers."

1. Prompt the user to enter the first number.
2. Read the input and convert it to an integer.
3. Prompt the user to enter the second number.
4. Read the input and convert it to an integer.
5. Calculate the value of multiplying the two numbers.
6. Print the value

Here is a full run of the program (user input is in blue)

This program multiplies two numbers.
Enter first number: 20
Enter second number: 3
60

In order to pass the tests you will need very specific prompts:
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

Don't forget to change these two values into integers.

This program is very similar to the example: Add Two Numbers 
Review that example and think about how you would change it to make it multiply instead of add.
"""


"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    # The main() calls the multiply() function. 
    multiply()

def multiply():
    # This function asks the user to input 2 integers and then it calculates their product.
    print("This program multiplies two numbers.")
    num1 = int(input('Enter first number: ')) # Why writing '1st'/'2nd' is not acceptable ?
    num2 = int(input('Enter second number: '))
    print(num1 * num2)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()