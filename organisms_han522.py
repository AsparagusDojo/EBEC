"""
Author: Near Han, han522@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/26/2022

Description:
    This program calculates population growth depends on data input by user.

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
    #Intake valuables
    start = float(input("Starting population, in thousands: "))
    inc = float(input("Average daily increase, in percent: "))
    days = int(input("Number of days to multiply: "))
    rate = 1 + inc / 100
    #Print Results
    print("Day   Approx. Pop")
    for i in range(0, days + 1):
        #Calculates total populations
        total = start * rate ** i
        print(f"{i:3}   {total:11.3f}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
