"""
Author: Near Han, han522@purdue.edu
Assignment: 01.1 - Road Trip
Date: 09/04/2022

Description:
    This program intakes diatance, price and fuel efficiency from user to calculate the
    total fuel price of the trip.

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
    print("Road trip fuel cost estimator:")
    #Ask for distance to destination
    dis = float(input("  How far away is your destination (miles)? "))
    #Ask for average gas price
    price = float(input("  What is the average price of gas (dollars per gallon)? "))
    #Ask for fuel efficiency
    mpg = float(input("  What is the fuel efficiency of your vehicle (mpg)? "))
    #Calculate fuel cost
    cost = int(2 * dis * price / mpg)
    #Return
    print(f"\nThe fuel cost for this trip is approximately ${cost}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
