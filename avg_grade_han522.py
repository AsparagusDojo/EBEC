"""
Author: Near Han, han522@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 10/03/2022

Description:
    This program intakes user's 5 grades inputs and calculates the average score then it will
    also determine the letter grade.

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
#Function for checking is the score entered is valid
def get_valid_score():
    grade = float(input("Enter a score: "))
    while grade < 0 or grade > 100:
        print("  Invalid Input. Please try again.")
        grade = float(input("Enter a score: "))
    return grade

#Define the average score of the grades entered
def calc_average(valid):
    sum = 0
    scope = len(valid)
    for i in range(0, scope):
        sum += valid[i]
    avg = sum / 5
    return avg

#Determine the letter grade based on average
def determine_grade(avg):
    if avg >= 92 and avg <= 100:
        letter = 'A'
    elif avg >= 82 and avg < 92:
        letter = 'B'
    elif avg >= 73 and avg <82:
        letter = 'C'
    elif avg >= 64 and avg < 73:
        letter = 'D'
    else:
        letter = 'F'
    return letter



def main():
    #Determine a list for storing thr 5 score
    valid = [0, 0, 0, 0, 0]
    for i in range(0,5):
        valid[i] = get_valid_score( )
        letter = determine_grade(valid[i])
        if i == 4:
            print(f"  The letter grade for {valid[i]:.1f} is {letter}.\n")
        else:
             print(f"  The letter grade for {valid[i]:.1f} is {letter}.")
    
    avg = calc_average(valid)
    final = determine_grade(avg)
    #Output Results
    print("\nResults:")
    print(f"  The average score is {avg:.2f}.")
    print(f"  The letter grade for {avg:.2f} is {final}.")




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
