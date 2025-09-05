"""
Write a program which asks a user to input an age in human years, and converts it to the 
equivalent age in dog years.
Dogs have different lifespans than humans. Thus their age is sometimes reported in "dog years" 
which are scaled to be comparable to human ages. On average every calendar year is equal to 
7.18 dog years. To convert 3 calendar years to dog years, you multiply 3 * 7.18 to get 
21.54 dog years. That means, if your dog is 3 years old, they're past their teenage years!

Your program will take in an age in calendar years, multiply that age by 7.18 and report the 
resulting dog years. Here's a sample run of the program (user input is in blue):

Enter an age in calendar years: 10
That's 71.8 in dog years!
"""

# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18  

def main():
    # The main() calls the age_calculator() function.
    age_calculator()

def age_calculator():
    """
    This function asks the user for age in calendar years, converts it into dog years 
    and lets the user know by printing it.
    """
    age_man= int(input('Enter an age in calendar years: '))
    age_dog= age_man * DOG_YRS_MULTIPLIER
    print("That's", age_dog, " in dog years!")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()