# Test Averages!!
# 5 Nov, 2017
# CTI-110 M6HW1 - Test Average and Grade
# James Griffith


def calcAverage( score1, score2, score3, score4, score5 ):
    average = ( score1 + score2 + score3 + score4 + score5 ) / 5
    return average

def determineGrade( studentScore ):
    if( studentScore < 60 ):
        return "F"
    elif( studentScore < 70 ):
        return "D"
    elif( studentScore < 80 ):
        return "C"
    elif( studentScore < 90 ):
        return "B"
    elif( studentScore < 101 ):
        return "A"

def askStudentScores():
    score1 = float( input( "Please enter the students first grade: " ) )
    score2 = float( input( "Please enter the students second grade : " ) )
    score3 = float( input( "Please enter the students third grade: " ) )
    score4 = float( input( "Please enter the students fourth grade : " ) )
    score5 = float( input( "Please enter the students fifth grade : " ) )

    return score1, score2, score3, score4, score5

def printTableOfResults( score1, score2, score3, score4, score5 ):
    print( "Score\tLetter Grade" )
    print( str( score1 ) + "\t\t" + determineGrade( score1 ), \
           str( score2 ) + "\t\t" + determineGrade( score2 ), \
           str( score3 ) + "\t\t" + determineGrade( score3 ), \
           str( score4 ) + "\t\t" + determineGrade( score4 ), \
           str( score5 ) + "\t\t" + determineGrade( score5 ), sep = "\n" )

def main():
    score1, score2, score3, score4, score5 = askStudentScores()
    print()
    printTableOfResults( score1, score2, score3, score4, score5 )
main()    
    
