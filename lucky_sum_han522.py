"""
Author: Near Han, han522@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 10/03/2022

Description:
    This program intakes user's input and calculate the sum of number cannot be divisible by 3 within
    the range provided by user.

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
#Function to calculate the lucky sum of the given number
def lucky_sum(var1, var2):
    sum = 0   
    if var1 < var2:
        for i in range(var1, var2+1):
            if i % 3 !=0:
                sum += i
    else:
        for i in range(var2, var1+1):
            if i % 3 !=0:
                sum += i
    return sum


def main():
    #Intake valuables from user
    var1 = int(input("Enter the first integer: "))
    var2 = int(input("Enter the second integer: "))
    sum = lucky_sum(var1, var2)
    #Output result
    print(f"The sum of the lucky numbers is {sum:,}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
