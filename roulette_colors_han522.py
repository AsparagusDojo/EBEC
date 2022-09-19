"""
Author: Near Han, han522@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/18/2022

Description:
    This program ask user to draw balls from certain pockets and return the color 
    of the ball in that pocket.
    
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


"""Write new functions below this line (starting with unit 4)."""


def main():
    #Ask user which pocket thet want to draw from
    pockets = int(input("Please choose a pocket number: "))
    even = pockets % 2
    #Green for pocket 0
    if pockets == 0:
        print(f"  Pocket number {pockets} is green.")
    #There are only 0-36 pockets
    elif (pockets < 0 or pockets > 36):
        print("  Invalid Input!")
    #Determine color of pockets
    elif (pockets >= 1 and pockets <= 10) or (pockets >= 19 and pockets <= 28):
        if even == 0:
                print(f"  Pocket number {pockets} is black.")
        else:
            print(f"  Pocket number {pockets} is red.") 
    elif (pockets >= 11 and pockets <= 18) or (pockets >= 29 and pockets <= 36):
        if even == 0:
                print(f"  Pocket number {pockets} is red.")
        else:
            print(f"  Pocket number {pockets} is black.")

        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
