import os
import csv

#init the recource's folder path
csvpath='Resources/budget_data.csv'

#open the csv file for reading
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)

    #read the file header
    header=next(csvreader)
    
    #initialize the analytical variables
    totalMonth=0
    totalProfit=0
    totalLosses=0
    profit_over_losses_change=0
    profit_greatest_increase=0
    profit_greatest_decrease=0

    #reading the csv data 
    for row in csvreader:
        #increment totalMonth after each row
        totalMonth+=1
        
        #for profit
        if int(row[1])>0:
            totalProfit+=int(row[1])
        #for losses
        else:
            totalLosses+=int(row[1])
        
    #print out the results 
    print('\n')
    print('Financial Analysis')
    print('-----------------------------------')
    print(f'Total Months: {totalMonth}')
    print(f'Total= {totalProfit+totalLosses}')
    



