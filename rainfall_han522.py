"""
Author: Near Han, han522@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/26/2022

Description:
    This program calculates the relative rainfall data for certain number of years.

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
    total = 0
    count = 0
    #Create a list of month names
    month = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
    #Ask iser how many years
    year = int(input("Enter the number of years: "))
    if year <= 0 :
        print("Invalid input; years must be greater than 0.")
    else:
        #Taking in rainfall data
        for i in range(1, year + 1):
            print(f"  For year No. {i}")
            for j in range(0, 12):
                rainfall = float(input(f"    Enter the rainfall for {month[j]}: "))
                while rainfall < 0:
                    print("    Invalid input; rainfall cannot be negative.")
                    rainfall = float(input(f"    Enter the rainfall for {month[j]}: "))
                total += rainfall
                count += 1

        #Output the results
        avg = total/count
        print(f"There are {count} months.")
        print(f"The total rainfall was {total:.2f} inches.")
        print(f"The monthly average rainfall was {avg:.2f} inches.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
