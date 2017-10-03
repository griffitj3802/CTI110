#James Griffith
#Mr Cameron
#CTI-110-0901
#M3T1


# Input the length and width of rectnagle 1.
length1 = int(input('Enter the length of rectanlge 1: '))
width1 = int(input('Enther the width of rectanlge 1: '))

# Input the length and width of rectangle 2.
length2 = int(input('Enter the length of rectanlge 2: '))
width2 = int(input('Enther the width of rectanlge 2: '))


# Calculate the area of rectangles
area1 = length1 * width1
area2 = length2 * width2

# CDetermine which one has the greater area
if area1 > area2:
    print('Rectangle 1 has the greatest area.')
elif area2 > area1:
    print('Rectangle 2 has the greastest area.')
else:
    print('Both rectanlges have the same area.')
