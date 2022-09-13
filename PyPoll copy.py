
# Add our dependencies.
import os
import csv
import datetime
import random
from sqlite3 import Row

# Set path for file
readfilepath=os.path.join('Resources','election_results.csv')
writefilepath=os.path.join('Resources','Elections Analysis.txt')

total_votes=0
candidates_list=[]
county_list=[]
candidate_votes={}
county_analysis={}


# Assign a variable to load a file from a path.
with open(readfilepath,"r") as election_results_csvfile:
    
    # Creating hadler for the file to perform read operations from csv file
    elections_data=csv.reader(election_results_csvfile,delimiter=",")

    for rows in elections_data :
        #counter to count total number of votes
        total_votes +=1
        # Print the candidate name from each row.
        candidate_name=rows[2]
        county_name=rows[1]
        #if condition to check if the name already exists
        if county_name not in county_analysis:
            county_analysis[county_name]={}
            county_analysis[county_name]["Candidates"]={}
            county_analysis[county_name]["Total Votes Occured"]=0
        
        if candidate_name not in candidates_list:
            # if not, add it to the list of candidates.
            candidates_list.append(candidate_name)
            candidate_votes[candidate_name]={}
            candidate_votes[candidate_name]["Total Votes"]=0
        
        if candidate_name not in county_analysis[county_name]:
            county_analysis[candidate_name]["Candidates"]=candidate_name


        print(county_analysis)
        # The total numbers of votes each candidate won
        candidate_votes[candidate_name]["Total Votes"] += 1
        county_analysis[county_name]["Total Votes Occured"] +=1
        # The percentage of votes each candidate won
        votes_percentage=candidate_votes[candidate_name]["Total Votes"]/total_votes*100
        candidate_votes[candidate_name]["Percentage"]=votes_percentage
        county_votes_percentage=county_analysis[county_name]["Total Votes Occured"]/total_votes*100
        county_analysis[county_name]["Voting Percentage"]=county_votes_percentage
    
with open(writefilepath,"w") as analysis_results_textfile:
    election_results_summary = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    )
    analysis_results_textfile.write(election_results_summary)
    #print(election_results_summary)

    winning_votes = 0
    winning_percentage = 0
    winning_candidate = " "
 
    for candidate_name in candidates_list:
        # A complete list of candidates who received votes
        analysis_results_textfile.write(f'{candidate_name}: {candidate_votes[candidate_name]["Percentage"]:.1f}% ({candidate_votes[candidate_name]["Total Votes"]:,})\n')
       # print(f'{candidate_name}: {candidate_votes[candidate_name]["Percentage"]:.1f}% ({candidate_votes[candidate_name]["Total Votes"]:,})\n')
        # The winner of the elections based on popular votes
        if candidate_votes[candidate_name]["Total Votes"] > winning_votes and candidate_votes[candidate_name]["Percentage"] > winning_percentage:
            winning_votes=candidate_votes[candidate_name]["Total Votes"]
            winning_percentage=candidate_votes[candidate_name]["Percentage"]
            winning_candidate=candidate_name

    winning_candidate_summary=(
         f"-------------------------\n"
         f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_votes:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    analysis_results_textfile.write(winning_candidate_summary)
    #print(winning_candidate_summary)

election_results_csvfile.close()
analysis_results_textfile.close()