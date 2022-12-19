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
