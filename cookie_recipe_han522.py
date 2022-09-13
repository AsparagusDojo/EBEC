"""
Author: Near Han, han522@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 09/04/2022

Description:
    This program intakes user's request of how many cookies to made and calculate
    the required materials of butter, sugar and flour respectively.

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
    #Ask number of cookies being made
    number = int(input("How many cookies do you want to make? "))
    #Return results
    print(f"To make {number:,} cookies, you will need:")
    #Number of cups of butter
    butter = number / 48 * 1.25
    print(f"{butter:10,.2f} cups of butter")
    #Number of cups of sugar
    sugar = number / 48 * 1.5
    print(f"{sugar:10,.2f} cups of sugar")
    #Number of cups of flour
    flour = number / 48 * 2.5
    print(f"{flour:10,.2f} cups of flour")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
