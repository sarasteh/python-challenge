

# PyBank 
Here I create a python code to analyze the financial records, given in  **budget_data.csv**. This csv file includes two columns,_"Date"_ and _"Profit/Losses"_.The following information are gathered from the data.

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

The final script print the analysis to the terminal and also export a text file(log.txt) with the results.

This folder includes the following :
*  analysis
   * ##### log.txt (output results)
* Resources
   * ##### budget_data.csv
* main.py 


---------------------
>##          main.py
-------------------------

  ```python
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
  ```
-----------------------
### Output is as follows:

-----------------------



```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```


# PyPoll 

In PyPoll, I create a Python script that analyzes the voting results given in **election_data.csv**. The csv file is inside the **PyPoll/Resources**. The file contains three columns,_"Voter ID", "County", and "Candidate"_.Using these information, the following outputs will be created:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

The final script print the analysis to the terminal and also export a text file(log.txt) with the results.

This folder includes the following :
*  analysis
   * ##### log.txt (output results)
* Resources
   * ##### election_data.csv
* main.py 


---------------------
>##          main.py
-------------------------
```python
import os
import csv

#set the input data file's path
csvpath='Resources\election_data.csv'

#set the log file path
log_file_path='analysis\log.txt'

#initialize the variables
total_votes=0
section_line='------------------------'

#create a dictionary to store candidates' info
election_results = {'candidate_name':[],
'number_of_votes':[] }


#read the csv file
with open(csvpath) as csvfile:
    input_file=csv.reader(csvfile)
    
    #read the file header
    header=next(input_file)

    for row in input_file:
        #update the number of votes
        total_votes+=1
       
        #if the candidate name's already there, update her/his informatio, 
        # otherwise append her/his name to the list   
        if row[2] in election_results['candidate_name']:
            index=election_results['candidate_name'].index(row[2])
            election_results['number_of_votes'][index]+=1
        else:
            election_results['candidate_name'].append(row[2])
            election_results['number_of_votes'].append(1)

    
    output_list=['Election Results',
    section_line,
    f'Total Votes: {total_votes}',
    section_line
    ]
     
    
    current_index=0
    max_votes=0
    winner_index=0
    #add candidates' info to the output list
    for candidate in election_results['candidate_name']:
        number_of_votes= election_results["number_of_votes"][current_index]
        percentage=round(100*number_of_votes/total_votes,3)
        output_list.append(f'{candidate}: {percentage}% ({number_of_votes})')

        #look for the winner
        if number_of_votes>max_votes:
            max_votes=number_of_votes
            winner_index=current_index
        
        current_index+=1
    
    #add winner's name to the output list
    output_list.append(section_line)
    output_list.append( f'Winner: {election_results["candidate_name"][winner_index]}')
    output_list.append(section_line)

    

    #print out the results to the terminal
    for output in output_list:
        print(output)

    #write the results in the log file
    with open(log_file_path,'w') as log_file:
        for output in output_list:
            log_file.write(output)
            log_file.write('\n')

```

-----------------------
### Output is as follows:

-----------------------

  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```

