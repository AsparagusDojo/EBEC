"""
Author: Near Han, han522@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/18/2022

Description:
    This program intakes number of package willing to purchase and calculate the price
    after discounting.

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


from os import NGROUPS_MAX


def main():
#Asks user the amount of package they are purchasing
    purchase = int(input("How many packages will be purchased: "))

    #Determine the discount amount by the number that user is purchasing
    #Purchase number cannot be negative
    if purchase < 0:
        print("  Invalid Input!")
    elif (purchase >= 0 and purchase <=3):
        print("  No discount applied.")
         #Calculating the toal price of the package purchased
        price = purchase * 880
        #Output results of total price
        print(f"  The total price to purchase {purchase} packages is ${price:,.2f}.")
    elif(purchase >= 4 and purchase <= 39):
        discount = 10
        price = purchase * 880 * (1 - discount / 100)
        print(f"  {discount}% discount applied.")
        print(f"  The total price to purchase {purchase} packages is ${price:,.2f}.")
    elif(purchase >= 40 and purchase <= 199):
        discount = 15
        price = purchase * 880 * (1 - discount / 100)
        print(f"  {discount}% discount applied.")
        print(f"  The total price to purchase {purchase} packages is ${price:,.2f}.")
    elif(purchase >= 200 and purchase <= 999):
        discount = 30
        price = purchase * 880 * (1 - discount / 100)
        print(f"  {discount}% discount applied.")
        print(f"  The total price to purchase {purchase} packages is ${price:,.2f}.")
    else:
        discount = 42
        price = purchase * 880 * (1 - discount / 100)
        print(f"  {discount}% discount applied.")
        print(f"  The total price to purchase {purchase} packages is ${price:,.2f}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
