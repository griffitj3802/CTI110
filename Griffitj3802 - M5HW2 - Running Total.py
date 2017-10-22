#Griffith James
#Mr. Cameron
#CTI-110 0901
#Oct 18, 2017

runningTotal = 0
realTotal = 0
gradeVariable = ""

print("Enter '-1' to exit or enter a score")
while gradeVariable != "-1":
    gradeVariable = input("Enter a grade or '-1' to exit:" )
    if gradeVariable == "-1":
        break
    runningTotal += int(gradeVariable)
    realTotal += 1
    
print(" Our total is: ", runningTotal)

