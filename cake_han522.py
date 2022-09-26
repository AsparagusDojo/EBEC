"""
Author: Near Han, han522@purdue.edu
Assignment: 03.1 - Cakes
Date: 09/26/2022

Description:
    This program prints a certain layer of pyrimid as user input.

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
    #Intake number of layer
    n = int(input("Enter the number of layers: "))
    space = n
    #Count printing rows
    for i in range(0, n):
        #Print leading space
        for j in range(0, space):
            if j == space - 1:
                print("[", end = "")
            else:
                print(end = " ")             
        space = space - 1
        if space == -1:
            print("[", end = "")
        #Printing stars
        for k in range(0, 2*i+1):
            print("*", end = "")
        print("]")
        print("\r")
 
    # for i in range(n): print(f"{'*'*(2*i+1):>{n+i}}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
