# A guessing game!!
# 10 Nov, 2017
# CTI-110 M6HW2 - Random Number Guessing Game
# James Griffith
# Mr. Cameron

import random
print("It's a guessing game")

def generateRandomNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber

def askUserForNumber( message = "How many Pickles? " ):
    userNumber = int( input( message ) )
    return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too many pickles, Morty"
    elif userNumber < randomNumber:
        return "Not enough pickles, Morty!"
    else:
        return "You did it!"
    

def main():
    userCongratulated = False  
    letsStart = True

    while userCongratulated or letsStart:
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        userNumber = askUserForNumber()
        userNumberOfGuesses += 1
        message = checkUserNumber( userNumber, randomNumber )

        while message != "You did it!":
            print( message )
            userNumber = askUserForNumber( "Give me another number: " )
            userNumberOfGuesses = userNumberOfGuesses + 1 
            message = checkUserNumber( userNumber, randomNumber )
            

            
        print()
        print( message, "It took you", userNumberOfGuesses,\
               "attempts to guess the pickles!\n" )
        userCongratulated = True

userNumber = input()
if userNumber.lower() == "end":

    MM = float(userNumber)
main()
