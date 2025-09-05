"""
Nimm is an ancient game of strategy that is named after the old German word for "take." 
It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate 
taking stones until there are zero left. The game of Nimm goes as follows:

The game starts with a pile of 20 stones between the players
The two players alternate turns
On a given turn, a player may take either 1 or 2 stone from the center pile
The two players continue until the center pile has run out of stones.
The last player to take a stone loses.

Write a program to play Nimm. To make your life easier we have broken the problem down into 
smaller milestones. You have a lot of time for this program. Take it slowly, piece by piece.

Milestone 1

Start with 20 stones. Repeat the process of removing stones and printing out how many stones are left until there are zero. Don't worry about whose turn it is. Don't worry about making sure only one or two stones are removed. Use the method int(input(msg)) which prints msg and waits for the user to enter a number and casts it to an integer. Add an empty print() function between removals to make  tracking turns easier. This should look like (user input is in blue):

There are 20 stones left.
Would you like to remove 1 or 2 stones? 2

There are 18 stones left.
Would you like to remove 1 or 2 stones? 17

There are 1 stones left.
Would you like to remove 1 or 2 stones? 3

Game over


Milestone 2

Create a variable of type int to keep track of whose turn it is (remember there are two players). Tell the user whose turn it is. Each time someone picks up stones, change the player number. With this, your output should now be (user input is in blue):

There are 20 stones left.
Player 1 would you like to remove 1 or 2 stones? 1

There are 19 stones left.
Player 2 would you like to remove 1 or 2 stones? 1

There are 18 stones left.
Player 1 would you like to remove 1 or 2 stones? 17

There are 1 stones left.
Player 2 would you like to remove 1 or 2 stones? 1

Game over


Milestone 3

Make sure that each turn only one or two stones are removed. After you read a number of stones 
to remove from a user (their input), you can use the following pattern to check if it was valid 
and keep asking until it is valid.

while (input_is_invalid) :
   user_input = int(input("Please enter 1 or 2: "))

Now, instead of the output Milestone 2 gave you, the output should now be (user input is in blue):

There are 20 stones left.
Player 1 would you like to remove 1 or 2 stones? 1

There are 19 stones left.
Player 2 would you like to remove 1 or 2 stones? 1

There are 18 stones left.
Player 1 would you like to remove 1 or 2 stones? 17
Please enter 1 or 2: 2

There are 16 stones left.
Player 2 would you like to remove 1 or 2 stones? 1

... (the game continues)


Milestone 4

Announce the winner.

... (outputs that should be handled in Milestone 1-3)

There are 1 stones left.
Player 1 would you like to remove 1 or 2 stones? 1

Player 2 wins!


Extensions

Can you write an AI opponent? You can start with a dummy AI that always plays a random number. 
Then try to make one that plays intelligently...

Some other extension ideas:

Make sure that if there is only one stone left, the last player may only remove one stone

Give the user the option for the winner to be the player that doesn’t take the last stone, 
or the player that does take the last stone.

Expand the game to let players take 1, 2, or 3, stones per turn.

Divisible by 3 rule: if the number of stones remaining at the end of a player’s turn is divisible 
by 3, they must go again.

Give the user the option to play against the computer and design a process for the computer to 
choose how many stone to remove.

Come up with your own extension!
"""

TOTAL_STONES = 20
stone_removal_prompt = ' would you like to remove 1 or 2 stones? '

def main():
    # Step 1  
    remaining_stones = TOTAL_STONES

    # Conducts the game of Nimm 
    play_nimm_game(remaining_stones)
    
    

def play_nimm_game(remaining_stones) :
    """
    How the Program Works 
    ---------------------
    Steps :
    1. Starts with 20 stones, player 1 being 1st to play.
    2. Program asks from the 2 players alternately about how many stones each would like 
       to remove -- 1 or 2. If any other number is passed, the program specifically asks
       for a choice between 1 or 2, repeating the command unless the conditions are met.
    3. With each turn, the remaining no. of stones and player type -- 1 or 2, is updated. 
    4. When there are 0 stones left, the user checks the player type in the last turn. 
       If it was player 1, then player 2 wins and vice-versa. The program then breaks from 
       the loop. 
    """

    current_player = 1 
    stones_to_remove = 0  

    make_choice(remaining_stones, current_player, stones_to_remove)

def make_choice(remaining_stones, current_player, stones_to_remove) :
    # Steps 2 & 3 at play 
    while remaining_stones > 0 and remaining_stones <= 20 :            
        # Step 2
        print('There are', str(remaining_stones), 'stones left.')
        stones_to_remove = int(input('Player '+ str(current_player) + stone_removal_prompt))
        # while loop to ensure the user enters either '1' or '2' as input
        while (stones_to_remove != 1 and stones_to_remove != 2) :
            stones_to_remove = int(input('Please enter 1 or 2: '))
        # updating how many stones are left
        remaining_stones -= stones_to_remove    
         
        check_player(remaining_stones, current_player)
        
        # Step 3 : Updating which player will play the next turn
        if current_player == 1 :
            current_player += 1
        else :
            current_player -= 1
        # blank print statement to ensure there's space between each turn : readability
        print()

def check_player(remaining_stones, current_player) :
    # Step 4 : When there are no (0) stones
    # Checks which player was in the last turn and updates the player type accordingly
    if remaining_stones == 0 :
        if current_player == 1 :
            current_player += 1
        elif current_player == 2 :
            current_player -= 1
        # blank print statement to ensure there's space between each turn : readability
        print()
        print('Player '+ str(current_player) + ' wins!')


''' 
Python boilerplate code : Ensures the main function runs only when this module is 
executed as the main program, not when imported as a module. 
'''
if __name__ == '__main__':
    main()