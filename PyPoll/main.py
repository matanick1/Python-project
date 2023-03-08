import os
import csv


# Create a variable for the path to the CSV file
csvpath =  (r'C:\Users\mybub\Dropbox\PC\Desktop\python-challenge\PyPoll\Resources\election_data.csv')

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

    # set initial ballot id count to zero
    ballot_id_count = 0

    # make a list of all the candidate vote results
    candidate_votes_list = []

    # make a list of unique candidates
    unique_candidates = []

    # make a list of vote counts per candidate
    vote_counts_per_candidate_list = []

    # make a list of vote percentages per candidate
    vote_percentages_per_candidate_list = []

    #loop through the rows
    for row in reader:

    # count the rows in "reader". Each row is a vote
        ballot_id_count = ballot_id_count +  1

    # add all the candidate votes to the candidate list
        candidate_votes_list.append(row[2])

    # loop through the list of "candidate vote list" to find all 
    # of the candidates that received votes. The set() function 
    # "sees" everything in the list, but only returns unique 
    # values
    for names in set(candidate_votes_list):

    # add the results of the "set" loop to the unique candidates
    # list. Since we're still in the "set" loop, the loop "sees"
    # all of the names in the list, but only returns unique
    # values. In this case, unique names
        unique_candidates.append(names)
    
    # count the amount of votes per candidate. Since we're still
    # in the "set" loop, the loop "sees" all of the names in the
    # list, but when you use the "count" function, it is counting
    # how many times each unique name appears
        votes_per = candidate_votes_list.count(names)

    # add those values to the votes per candidate list
        vote_counts_per_candidate_list.append(votes_per)

    # find the percentage of votes per candidate
        percentage_per = (votes_per/ballot_id_count) * 100

    # add those values to the percentage per candidate list
        vote_percentages_per_candidate_list.append(percentage_per)

    # use this formula to convert many decimals to 3 decimals
        percentage_per = "%.3f%%" % percentage_per
       
    # winner equals largest vote count*************doesnt' work
       # winner_total =  max(votes_per)
        
    # print report

    print(f'Election Results \n')
    print(f'----------------------------------------------- \n')
    print(f'Total Votes: {ballot_id_count} \n')
    print(f'----------------------------------------------- \n')
    # for values in range(len(unique_candidates)):
        # print(f'{unique_candidates[values]}: {vote_percentages_per_candidate_list[values]} {vote_counts_per_candidate_list[values]}')
    
    # for index, value in enumerate(unique_candidates):
        # print(f'{unique_candidates[index]}: {vote_percentages_per_candidate_list[index]} {vote_counts_per_candidate_list[index]}')

    for i, word in enumerate(vote_percentages_per_candidate_list):
        print(i, word)


    
        
        
       
   
    

    
        
    

