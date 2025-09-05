"""
Write a program that asks a user to enter a number. Your program will then double that number 
and print out the result. It will repeat that process until the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4
8
16
32
64
128

Note that: 
2 doubled is 4
4 doubled is 8
8 doubled is 16 and so on.

We stop at 128 because that value is greater than 100.
Maintain the current number in a variable named curr_value. When you double the number, you 
should be updating curr_value. Recall that you can double the value of curr_value using a line 
like:
curr_value = curr_value * 2

This program should have a while loop and the while loop condition should test if curr_value 
is less than 100. Thus, your program will have the line:
while curr_value < 100:
"""

def main():
    # The main() calls the double_no() function.
    double_no()
    
def double_no():
    """
    This function asks a number from the user, doubles it and prints it in a cycle until 
    the value reaches 100 or greater. 
    """
    # Asks the user for a number.
    curr_value = int(input("Enter a number: "))
    # The while loop will work as long as curr_value < 100.
    while curr_value < 100 :
        # Prints its double.(Although curr_value is used, its value remains unmodified.)
        print(str(curr_value*2)) 
        # Uprgades the value of the variable curr_value by multiplying it with 2.
        curr_value*= 2 

    

if __name__ == '__main__':
    main()