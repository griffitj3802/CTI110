#James Griffith
#Mr. Cameron
#CTI-110-0901
#23 Sept 2017
#M3HW2 - Software Sales

# a simple program using main()



userNumberOfPackages = int( input("Please enter the number of pack" + \
                                   "ages bought: " ) )
packagePrice = 99

if userNumberOfPackages < 10:
    discount = 0;
elif userNumberOfPackages < 20:
    discount = 0.10;
elif userNumberOfPackages < 50:
    discount = .20;
elif userNumberOfPackages < 100:
    discount = 0.30;
else:
    discount = 0.40;

subTotal = userNumberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print("\nAmout of discount: $" + format( discountAmount, ",.2f" ) + \
      "\nTotal amount: $" + format( total, ",.2f" ) )



