#Griffith James
#Mr. Cameron
#CTI-110 0901
#Oct 18, 2017
#M5H3 - Factorials

ourInput = int(input(" Enter a nonnegative integer: "))

while ourInput < 1:
    ourInput = int( input( "Only Positive numbers: "))
    
factorial = 1

for i in range( 1, ourInput + 1 ):
    factorial = factorial * i

print( "The factorial of ", ourInput, "is", factorial )

