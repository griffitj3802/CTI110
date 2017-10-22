#Griffith James
#Mr. Cameron
#CTI-110 0901
#Oct 19, 2017
#M5HW1 - Distance and Speed!

carSpeed = float( input("What is the speed of the car?: "))
hoursTraveled = int( input("How many hours has the car traveled?: "))

print( "Hour","\tDistance Traveled")
for currentHour in range(1, hoursTraveled + 1):
    distanceTraveled = carSpeed * currentHour
    print( currentHour,"\t",distanceTraveled)
