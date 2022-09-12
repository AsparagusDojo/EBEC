"""
Author: Near Han, han522@purdue.edu
Assignment: 01.2 - Interest
Date: 09/09/2022

Description:
    This program intakes intial deposits, interest rate, number of years earn interest
    and number of times per year the interest is compounded to calculate the future 
    value deposit.

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
    print("Enter the following parameters.")
    #Ask for initial deposit
    P = float(input("  The initial deposit? "))
    #Ask for inerest rate in percent
    rate = float(input("  The annual interest rate in percent? "))
    #Ask for number of years the account earns interest
    t = float(input("  The number of years the account earn interest? "))
    #Ask for number of times the interest is compound
    n = float(input("  The number of times interest is compounded each year: "))
    r = rate / 100

    #Calculate ffuture balance
    FV = float(P * ((1 + r / n) ** (n * t)))
    #Return
    print(f"The balance of this account will be ${FV:,.2f} after {t:.1f} years.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
