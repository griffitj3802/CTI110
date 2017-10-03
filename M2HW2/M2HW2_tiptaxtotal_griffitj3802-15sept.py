
#James Griffith
#CTI 110-0901
#M2HW2 - Tip Tax Total
#15Sept2017
#In this excersice we created an easy tip machine. 
foodCost= float( input( "Cost of food: "))

tipAmount= 0.18 * foodCost

salesTax= 0.07 * foodCost

totalCost = foodCost + tipAmount + salesTax
print( "foodCost: $" + format( foodCost, ",.2f"), "Tip: $" + \
        format( tipAmount, ",.2f" ), "Sales Tax: $" + format( salesTax, ",.2f"), \
        "Total: $" + format( totalCost, ",.2f"), sep = "\n" )

        
