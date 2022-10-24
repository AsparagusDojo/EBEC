"""
Author: Near Han, han522@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/24/2022

Description:
    This program generates a random 2 digits integer and a 3 digits integer to be as a
    addition math quiz to test the user.

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
def random_number (num):
    start = 10 ** (num-1)
    end = (10 ** num)-1
    return random.randint(start, end)

def main():
    #Generates a random 2 digits number
    two = random_number(2)
    #Generates a random 3 digits number
    three = random_number(3)
    #Print the quiz
    print(f"{two: 5}")
    print(f"+ {three}")
    print("-----")
    correct = two + three
    ans = int(input("= "))
    #Check if user entered the right answer
    if ans == correct:
        print("Correct -- Good Work!")
    else:
        print(f"Incorrect. The correct answer is {correct}.")
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
