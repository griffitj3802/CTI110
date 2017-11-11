# A program that converts feet to inches!
# 5 Nov, 2017
# CTI-110 M6T2_FeetToInches 
# James Griffith
INCHES_PER_FOOT = 12

def main():
    feet = int(input("Please enter a number in feet: "))

    print(feet, "equals", feet_to_inches(feet), "inches.")

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
main()
