"""
Author: Near Han, han522@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/26/2022

Description:
    This program intakes numbers from users to calculate their sum and average.

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
    #Take in numbers
    initial = float(input("Enter a non-negative number (negative to quit): "))
    sum = 0
    count = 0
    #If first number entered is negative
    if initial < 0:
        print("  You didn't enter any numbers.")
    else:
        while initial >= 0:
            sum += initial
            count += 1
            initial = float(input("Enter a non-negative number (negative to quit): "))
    if sum != 0:
        avg = sum / count
        #Output results
        print(f"  You entered {count} numbers.")
        print(f"  Their sum is {sum:.3f} and their average is {avg:.3f}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
