"""
Author: Near Han, han522@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/18/2022

Description:
    This program intakes user's input to determine if it is
    a leap year and returns the number of days of February.
    
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
    #Takes input from user
    year = int(input("Enter a year: "))
    #Check if input year is divisible by 100 or 4
    check100 = year % 100
    check4 = year% 4

    # Check leap year fo year divisible by 100
    if check100 == 0:
        check400 = year % 400
        if check400 == 0:
            print(f"The year {year} is a leap year.")
            print(f"February of {year} has 29 days.")
        else:
            print(f"The year {year} is not a leap year.")
            print(f"February of {year} has 28 days.")
    
    #Check leap year for year not divisible by 4
    else:
        if check4 == 0:
            print(f"The year {year} is a leap year.")
            print(f"February of {year} has 29 days.")
        else:
            print(f"The year {year} is not a leap year.")
            print(f"February of {year} has 28 days.")
    
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
