import os
import csv

#initialize the resource's folder path
csvpath='Resources/budget_data.csv'

#open the csv file for reading
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)

    #read the file header
    header=next(csvreader)
    
    #initialize the analytical variables
    totalMonth=0
    total_profit_loss=0
    profit_over_losses_change=0
    profit_greatest_increase=0
    profit_greatest_decrease=0
    profit_greatest_increase_month=''
    profit_greatest_decrease_month=''
    total_change=0

    #reading the csv data 
    for row in csvreader:
        #increment totalMonth after each row
        totalMonth+=1
        
        #calculate the changes in profit/losses
        if totalMonth>1:
            change=int(row[1])-last_Profit_Loss
            total_change+=change

            #find the greatest increase in profit and its month
            if change>profit_greatest_increase:
                profit_greatest_increase=change
                profit_greatest_increase_month=row[0]
            
            #find the greatest decrease in profit and its month
            if change<profit_greatest_decrease:
                profit_greatest_decrease=change
                profit_greatest_decrease_month=row[0]

        #find the total profit/losses
        total_profit_loss+=int(row[1])
       
        #store the last month's profit/loss
        last_Profit_Loss=int(row[1])
    
    average_change=round(total_change/(totalMonth-1),2)


    #creating the output list 
    output_list=[
    'Financial Analysis',
    '-----------------------------------',
    f'Total Months: {totalMonth}',
    f'Total: ${total_profit_loss}',
    f'Average Change: ${average_change}',
    f'Greatest Increase in Profits: {profit_greatest_increase_month} (${profit_greatest_increase})',
    f'Greatest Decrease in Profits: {profit_greatest_decrease_month} (${profit_greatest_decrease})',]
    
    #print out the results to the terminal
    for output in output_list:
        print(output)
        
    #write the results in a log file    
    with open('analysis/log.txt','w') as log_file:
        for line in output_list:
            log_file.write(line)
            log_file.write('\n')