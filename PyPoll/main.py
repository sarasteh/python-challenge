import os
import csv

#set the input data file's path
csvpath='Resources\election_data.csv'

#set the log file path
log_file_path='analysis\log.txt'

#initialize the variables
total_votes=0


with open(csvpath) as csvfile:
    input_file=csv.reader(csvfile)
    
    #read the file header
    header=next(input_file)

    for row in input_file:
        total_votes+=1

    output_list=['Election Results',
    '-----------------------',
    f'Total Votes: {total_votes}'
    ]

    #print out the results to the terminal
    for output in output_list:
        print(output)

    #write the results in the log file
    with open(log_file_path,'w') as log_file:
        for output in output_list:
            log_file.write(output)
            log_file.write('\n')
