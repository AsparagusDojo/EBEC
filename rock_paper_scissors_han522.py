"""
Author: Near Han, han522@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/24/2022

Description:
    This program randomly generates a choice and play the game rock, paper, scissors
    with the user.

Contributors:
    N/A

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import random

"""Write new functions below this line (starting with unit 4)."""
#This function generates the computer's pick within rock, paper, scissors
def get_computer_choice ():
    list = ['rock', 'paper', 'scissors']
    pick = random.choice(list)
    return pick


#This function gets user's input
def get_player_choice():
    user = input("Choose rock, paper, or scissors: ")
    while user != 'rock' and user != 'paper' and user != 'scissors':
        print("You made an invalid choice. Please try again.")
        user = input("Choose rock, paper, or scissors: ")
    return user

#Determine winner of the game
def get_winner(comp, user):
    if comp == 'rock':
        if user == 'rock':
            results = 'tie'
        elif user == 'paper':
            results = 'player'
        else:
            results = 'computer'
    elif comp == 'paper':
        if user == 'paper':
            results = 'tie'
        elif user == 'rock':
            results = 'computer'
        else:
            results = 'player'
    elif comp == 'scissors':
        if user == 'scissors':
            results = 'tie'
        elif user == 'paper':
            results = 'computer'
        else:
            results = 'player'
    return results

def main():
    comp = get_computer_choice()
    user = get_player_choice()
    print(f"  The computer chose {comp}, and you chose {user}.")
    results = get_winner(comp, user)
    #Game keep going till tie is broken
    while results == 'tie':
        print("It's a tie. Starting over.\n")
        comp = get_computer_choice()
        user = get_player_choice()
        print(f"  The computer chose {comp}, and you chose {user}.")
        results = get_winner(comp, user)
    if results == 'computer':
        print(f"  {comp} beats {user}")
        print("  You lost. Better luck next time.")
    elif results == 'player':
        print(f"  {user} beats {comp}")
        print("  You won the game!")
    print("Thanks for playing.")

    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
