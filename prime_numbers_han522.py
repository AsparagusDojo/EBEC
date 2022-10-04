"""
Author: Near Han, han522@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 10/04/2022

Description:
    This program intakes user's input to check if it is prime number.

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
#Function to check if the number is prime
def is_prime(num):
    if num > 1:
   # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                return 0
                break
            else:
                return 1
    else:
        return 0


def main():
    #Intake number from user
    num = int(input("Enter a positive integer (-1 to quit): "))
    #Check if each number is prime until user wants to quit
    while num != -1:
        check = is_prime(num)
        if check:
            print(f"  {num} is prime!")
        else:
            print(f"  {num} is not prime.")
        num = int(input("Enter a positive integer (-1 to quit): "))
        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
