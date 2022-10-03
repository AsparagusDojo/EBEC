"""
Author: Near Han, han522@purdue.edu
Assignment: 04.1 - Falling
Date: 10/03/2022

Description:
    This program outputs the result of the falling distance on a certain planet.

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
def falling(time):
    distance = 8.87 * (time ** 2) / 2
    print(f"{time:8}  {distance:12.1f}")

def main():
    #Time starts at 5 seconds
    start = 5
    print("Time (s)  Distance (m)")
    print("----------------------")
    #Track the results from 5 to 50 seconds
    while start <= 50:
        falling(start)
        start += 5


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
