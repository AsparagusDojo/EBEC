"""
Author: Near Han, han522@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/30/2022

Description:
    This program intakes a single integer and a list of integers. It then checks if the list
    of the number is divisible by the single integer and return the list of multiples.

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
#Function to determine what number in the list is the multiple of the integer
def multiples_of(mult, l):
    results = []
    index = len(l)
    for i in range(0,index):
        if l[i] % mult == 0:
            results.append(l[i])
    return results

def main():
    #Definition of the input numbers
    mult = 13
    l = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]

    #Results displaying
    print("Original list of numbers: ")
    print(f"  {l}")
    results = multiples_of(mult , l)
    print("Numbers in the list that are multiples of 13: ")
    print(f"  {results}")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
