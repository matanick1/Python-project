import os
import csv

# Create a variable for the path to the CSV file
CSV_PATH =  os.path.join('Resources', 'election_data.csv')
# Specify the file to write to
RESULTS_PATH = os.path.join('Analysis', 'Results.txt')

# Change the working directory to the location of the script
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Open the file and store the contents in the
# variable "CSV_PATH"
with open(CSV_PATH) as csvfile:

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

    # use this formula to convert many decimals to 3 decimals
        percentage_per = "%.3f%%" % percentage_per
    
    
    # add those values to the percentage per candidate list
        vote_percentages_per_candidate_list.append(percentage_per)
   
    # find the highest number of votes to determine winner
        most_votes = max(vote_counts_per_candidate_list)

    # print report

    print(f'Election Results \n')
    print(f'----------------------------------------------- \n')
    print(f'Total Votes: {ballot_id_count} \n')
    print(f'----------------------------------------------- \n')
   
    #   Enumerate function gives the index number and then the value of that index number. This loop is saying to loop through the unique
    #   candidates a find the index value of the candidate and then the candidate. Then, after looping, we're calling the index to print the 
    #   "0" value unique candidate, the "0" value vote percentage per candidate, and the "0" value vote count per candidate. Then it
    #   loops through the "1" value of all 3. And so on. 
    for index, name in enumerate(unique_candidates):
        print(f'{unique_candidates[index]}: {vote_percentages_per_candidate_list[index]} ({vote_counts_per_candidate_list[index]}) \n')

    print(f'----------------------------------------------- \n')
    
    # same concept as above. Loop through the vote count totals to find the index value of the vote count and the value of the vote count.
    for index, vote_count in enumerate(vote_counts_per_candidate_list):
    
    # Conditional to say if the vote count total of each index value is equal to the most votes then we print the unique candidate with
    # that same index. That is the winner
        if  vote_counts_per_candidate_list[index] == most_votes:
            print(f'Winner: {unique_candidates[index]} \n')

    
    print(f'----------------------------------------------- \n')

    # Open the file using "write" mode. Specify the variable to
    # hold the contents
    with open(RESULTS_PATH, 'w') as text:
        text.write(f'Election Results \n\n')
        text.write(f'----------------------------------------------- \n\n')
        text.write(f'Total Votes: {ballot_id_count} \n\n')
        text.write(f'----------------------------------------------- \n\n')
        for index, name in enumerate(unique_candidates):
            text.write(f'{unique_candidates[index]}: {vote_percentages_per_candidate_list[index]} ({vote_counts_per_candidate_list[index]}) \n\n')
        text.write(f'----------------------------------------------- \n\n')
        for index, vote_count in enumerate(vote_counts_per_candidate_list):
            if  vote_counts_per_candidate_list[index] == most_votes:
                text.write(f'Winner: {unique_candidates[index]} \n\n')
        text.write(f'----------------------------------------------- \n\n')
