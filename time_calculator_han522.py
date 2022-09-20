"""
Author: Near Han, han522@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/04/2022

Description:
    This program intakes number of seconds and convert it to days, hours and minutes.

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
    #Intake seconds from user
    sec = int(input("Please enter a time in seconds: "))
    
    #Determine days
    days = sec // 86400
    #Determine number of hours
    hours = sec % 86400 // 3600
    #Determine number of minutes 
    mins = sec % 3600 // 60
    #Determine seconds
    secleft = sec % 60

    #Output
    #If time is less than a minute
    if sec < 60:
        print(f"  {sec} seconds is less than one minute.")
    else:
        print(f'  {sec} seconds equals ', end = '')
        if days:
            print(f'{days} day(s)', end = '')

        if hours:
            if days:
                if mins or secleft:
                    print(', ', end = '')
                else:
                    print(' and ', end = '')
            print(f'{hours} hours(s)', end = '')

        if mins:
            if hours or days:
                if secleft:
                    print(', ', end = '')
                else:
                    print(' and ', end = '')
            print(f'{mins} minutes(s)', end = '')
        if secleft:
            if mins or hours or days:
                print(' and ', end = '')
            print(f'{secleft} seconds(s)', end = '')
        print('.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
