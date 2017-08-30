#CTI-110
#M2T1 - Sales Predicition
#James Griffith
#29 August 2017
#


# Get the project total sales.
total_sales = float( input ( 'Please enter the projected sales: '))

# Calculate the profit as 23 Percent of total sales
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))
