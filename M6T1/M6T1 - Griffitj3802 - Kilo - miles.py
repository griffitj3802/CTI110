# This program converts Kilometers to miles
# 4 Nov, 2017
# CTI-110 M6T1 - Convert Kilometers to Miles
# James Griffith
#
CONVERSION_FACTOR = 0.6214

#Two Fucntions are required.
def main():
    kilometers = float(input("Please input kilos for conversion: "))

    show_miles(kilometers)

def show_miles(km):
    miles = km * CONVERSION_FACTOR

    print(km, "kilometers equals",miles, "miles.")

main()
