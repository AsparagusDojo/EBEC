"""
Author: Near Han, han522@purdue.edu
Assignment: 04.5 - Prime List
Date: 10/03/2022

Description:
    This program intakes user's name from a specific selection pool and
    return greeting to the user.

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
import math

"""Write new functions below this line (starting with unit 4)."""
#Function to check if the number is prime
def is_prime(num):
    if num > 1:
   # check for factors
        for i in range(2, int(math.sqrt(num)) + 1):
            if (num % i) == 0:
                return False
                break
        else:
                return True
    else:
        return False


def main():
    #Create an empty list
    list = []
    limit = int(input("Enter a positive integer: "))
    start = 2
    #Takes upper limit from user
    print(f"The primes up to {limit} are: ", end = " ")
    #Checking and collecting list of prim
    for i in range(2, limit + 1):
        check = is_prime(i)
        if check:
            list.append(i)

    for j in range(0, len(list)):
        if j == len(list) - 1:
            print(list[j])
        else:
            print(f"{list[j]}, ", end = "")   
   
    
   

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
