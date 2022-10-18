"""
Author: Near Han, han522@purdue.edu
Assignment: 05.3 - Star Pattern
Date: 10/16/2022


Description:
    This program draws a color filled n-pointed star as user input.

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
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()


def main():
    #Determine the number of points on star
    pts = int(input("Points on the star: "))
    turn = 1
    #Determine angles
    A = 360 / pts
    B = 2 * A
    #Determine initial angle
    theta = 90 - A
    #Draw the star
    color('black', 'blue')
    begin_fill()
    right(theta)
    forward(60)
    while turn <= (2 * pts - 1):
        if turn % 2 == 1:
            left(180 - A)
            forward(60)
            turn += 1
        else:
            right(180 - B)
            forward(60)
            turn += 1
    end_fill()
    

    
"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
