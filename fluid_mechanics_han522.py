"""
Author: Near Han, han522@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/04/2022

Description:
    This program intakes user's input for temperature, flow velocity and pipe diameter
    to calculate Reynolds number.

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
    #Intakes temperature
    temp = int(input("Enter the temperature in °C as 5, 20, or 50: "))
    #Determine viscosity depends on temperature
    if temp == 5:
        vis = 1.52e-6
    elif temp == 20:
        vis = 1.00e-6
    elif temp == 50:
        vis = 5.54e-7
    #Intakes velocity and pipe diameter
    velocity = float(input("Enter the velocity of water in the pipe (m/s): "))
    piped = float(input("Enter the pipe's diameter (m): "))
    #Caculates Reynolds number
    re = velocity * piped / vis
    print(f"At {temp:.1f}°C, the Reynolds number for flow at {velocity} m/s in a {piped} m diameter pipe is {re:.2e}.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
