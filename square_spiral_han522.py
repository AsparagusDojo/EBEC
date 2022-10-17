"""
Author: Near Han, han522@purdue.edu
Assignment: 05.2 - Square Spiral
Date: 10/16/2022

Description:
    This program draws a square spiral from inside to ouside with a increment in length
    in each square.

Contributors:
    Name, login@purdue.edu [repeat for each]

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
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    #Length of first step
    initial = 12
    side = 1
    #Initial heading direction
    setheading(45)
    forward(initial)
    while side <= 28:
        right(90)
        #Step increases in length everytime it turns 90 degree
        initial += 12
        forward(initial)
        side += 1
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
