#James Griffith
#Mr Cameron
#23 Sept 2017
#M3LAB: Debugging

def main():
    print ("This program takes a number grade and outputs a letter grade." )
#   system uses 10-point grading scale
    
a_Score = 90-100
B_Score = 80-89
c_Score = 70-79
d_Score = 60-69
f_Score = 50-59
t_Score = 49-0
# To Do: define the rest of the scores

score = int(input("What is the test score: "))
if score >= 90:
    print ("the grade is: A")
elif score >= 80:
    print ("The grade is: B")
elif score >= 70:
    print ("The grade is: C")
elif score >= 60:
    print ("The grade is: D")
elif score >= 50:
    print ("The grade is: F")
elif score >= 0:
    print ("The grade is too low")
#To DO: Finish line

 
