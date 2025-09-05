"""
Code in Place is not only massive, but also super diverse! We serve a lot of students worldwide 
who speak many different languages. To practice our language skills, we want to make a helpful 
tool to help us study Spanish!

Write a program that loops over a dictionary of words and quizzes the user for their corresponding 
Spanish translations, keeping count of how many the user gets correct! Separate each question and 
answer with a blank line to help with visual clarity.

Here's a sample run of the program (user input is in blue):

What is the Spanish translation for hello? hola
That is correct!

What is the Spanish translation for dog? gato
That is incorrect, the Spanish translation for dog is perro.

... (quizzes user on the rest of the words)
That is correct!

You got 6/8 words correct, come study again soon!
"""

def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    num_correct = ask_question(translations)
    print_correct(num_correct)


def ask_question(dictionary) :
    """ 
    Asks the user for the Spanish translation of the English words in the dictionary
    and comments whether it is correct or not. If correct, then count of correct words 
    increases by 1. If not, then additionally displays the correct translation.
    """
    count = 0
    for key,value in dictionary.items() :
        translated = input('What is the Spanish translation for '+ key +' ?')
        if translated == value :
            print('That is correct!')
            count += 1
        else :
            print('That is incorrect, the Spanish translation for', key, 'is', value + '.' ) 
        print()
        
    return count

def print_correct(count) :
    # Prints how many out of the 8 words the user got correct.
    print('You got', str(count) + '/8 words correct, come study again soon!')

if __name__ == '__main__':
    main()