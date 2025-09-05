"""
In the game Fizz Buzz, players take turns counting up from one. If a player’s turn lands on a 
number that’s divisible by 3, she should say “Fizz” instead of the number, and if it lands on a 
number that’s divisible by 5, she should say “Buzz” instead of the number. If the number is both a 
multiple of 3 and of 5, she should say "Fizzbuzz" instead of the number. A spectator sport, it is 
not.
What it is, however, is an interesting problem in control flow and parameter usage. Write a 
function called fizzbuzz which accepts as a parameter an integer called n. The function should 
return what a player should say if it is the number n on their turn. Here are a few examples:

fizzbuzz(8) # returns 8
fizzbuzz(10) # returns "Buzz"
fizzbuzz(3) # returns "Fizz"

Next, complete your program by writing a main function that plays Fizz Buzz up to 17. Here's a 
sample run of the program:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizzbuzz
16
17

Recall that in order to check if a number is divisible by a value, you can use the remainder 
operator %. Want to check if some number n is divisible by 5? When you divide n by 5 the remainder 
should equal 0:
# checks if n is divisible by 5
is_divisible = n % 5 == 0
"""

MAX_VALUE = 17

def main():
    # Runs the Fizz Buzz game till 17 using a for loop.
    for i in range (MAX_VALUE) :
        result = fizzbuzz(i + 1)
        print(result)

def fizzbuzz(n):
    """
    Takes in a positive integer (n) and returns what the player should say at that value.
    If n is divisible by 3, then returns "Fizz" ;
    if n is divisible by 5, then returns "Buzz" ;
    if n is divisible by both 3 & 5, then returns "Fizzbuzz".
    For other nos., it returns the nos. themselves.    
    """
    if n % 3 == 0 and n % 5 == 0 :
        return "Fizzbuzz"
    elif n % 3 == 0 :
        return "Fizz"
    elif n % 5 == 0 :
        return "Buzz"
    else :
        return n

if __name__ == '__main__':
    main()