# This will allow me to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Create a variable for the path to the CSV file
csvpath = (r'C:\Users\mybub\Dropbox\PC\Desktop\python-challenge\PyBank\Resources\budget_data.csv')

# Open the file and store the contents in the
# variable "csvfile"
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable
    # that holds contents
    reader = csv.reader(csvfile, delimiter = ",")

    # single out the first line of "reader", which
    # is the header, and make it the variable
    # csv_header. It also skips, or "parses" the first row of the
    # data form now on. 
    csv_header= next(reader)

    # set initial month count to zero
    month_count = 0

    # set total for profit and losses
    total_profit = 0

    # set starting profit
    starting_profit = 0

    # set total profit change to zero to start
    total_profit_change = 0

    # create a list of the profit and losses
    profit_list = []

    # make a list to store the changes in profit from month
    # to month
    profit_change_list = []

    # make a list to store the dates
    date_list = []
    
    # loop through the rows
    for row in reader:  

    # count the rows in "data". Each row is a month
        month_count = month_count + 1
      
    # add up the profit and losses
        total_profit += int(row[1])
    
    # final profit for each row is the integer of the "1" value
    # column
        final_profit = int(row[1])

    # add to the profit list to get a list of each individual
    # monthly profit
        profit_list.append(int(row[1]))
        
    # change in profit from month to month
        month_to_month_profit = final_profit - starting_profit

    # add to the profit change list to get a list of each
    # individiual monthly profit changes
        profit_change_list.append(month_to_month_profit)

    
    # total change in profits because we need the average of 
    # the profit and losses over the entire period. This is
    # the first part of that equation
        total_profit_change = total_profit_change + month_to_month_profit

    # reset starting profit to what was the final profit because
    # we are about to restart the loop and do it all over again
    # down all the rows
        starting_profit = final_profit

    # find the average of the profits over the entire period
        average_profit = total_profit_change/month_count

    # add dates to the date list using the "0" value for the 
    # column
        date_list.append(row[0])

    # find the greatest increase in profits over the entire
    # period
        greatest_increase = max(profit_change_list)

    # find the index value of the greatest increase
        greatest_index_value = profit_change_list.index(greatest_increase)
        
    # find the date that correlates to the greatest increse in
    # profit
        date_greatest_increase = date_list[greatest_index_value]

    # find the greatest decrese in profits over the entire 
    # period
        greatest_decrease = min(profit_change_list)
    
    # find the index value of the greatest decrease
        greatest_decrease_index_value = profit_change_list.index(greatest_decrease)

    # find the date that correlates to the greatest decrease
        date_greatest_decrease = date_list[greatest_decrease_index_value]
        
   # print report

    print(f'Financial Analysis \n')
    print(f'----------------------------------------------- \n')
    print(f'Total Months: {month_count} \n')
    print(f'Total: ${total_profit} \n')
    print(f'Average Change: ${round(average_profit)} \n')
    print(f'Greatest Increase In Profits: {date_greatest_increase} ({greatest_increase}) \n')
    print(f'Greatest Decrease In Profits: {date_greatest_decrease} ({greatest_decrease}) \n')

    
    # Specify the file to write to
    results_path = (r"C:\Users\mybub\Dropbox\PC\Desktop\python-challenge\PyBank\Analysis\Results.txt")

    # Open the file using "write" mode. Specify the variable to
    # hold the contents
    with open(results_path, 'w') as text:

    # Write the rows
        text.write(f'Financial Analysis \n')
        text.write(f'----------------------------------------------- \n')
        text.write(f'Total Months: {month_count} \n')
        text.write(f'Total: ${total_profit} \n')
        text.write(f'Average Change: ${round(average_profit)} \n')
        text.write(f'Greatest Increase In Profits: {date_greatest_increase} ({greatest_increase}) \n')
        text.write(f'Greatest Decrease In Profits: {date_greatest_decrease} ({greatest_decrease}) \n')
        
        
    

        
        



    