
# Add our dependencies.
import os
import csv

# Set path for file to read
readfilepath=os.path.join('Resources','election_results.csv')
# Set path for file to write
writefilepath=os.path.join('Resources','Elections_Analysis.txt')

total_votes=0 #Counter to counnt total number of votes polled
candidate_list=[] # initialized a list to store names of Candidates
county_list=[] # initialized a list to store name of counties
candidate_analysis={} #  Empty dictionary to store various keys and values of a candidate
county_analysis={} # Empty dictionary to store various keys and values of a county

# Assign a variable to load a file from a path.
with open(readfilepath,"r") as election_results_csvfile:
    
    # Creating hadler for the file to perform read operations from csv file
    elections_data=csv.reader(election_results_csvfile,delimiter=",")
    #Read Header
    iter_election_data = iter(elections_data)
    next(iter_election_data)

    for rows in iter_election_data   :
        #counter to count total number of votes
        total_votes +=1
        # Print the candidate name from each row.
        candidate_name=rows[2]
        # Get the county name from each row and store in a variable name county_name
        county_name=rows[1]

        # Conditional statement to check if county name already exists in county_list
        # If not, add county name to county list and initializing dictionary of county name under dictionary county_analysis 
        if county_name not in county_analysis:
            county_list.append(county_name)
            county_analysis[county_name]={}
            # Adding keys and values to dic after initializing
            county_analysis[county_name]={"County Votes":0,"County Percentage":0}

        # Conditional statement to check if candidate name already exists in county_list[county name] dictionary
        # If not,initializing dictionary of candidate name under dictionary county_analysis[county name]
        if candidate_name not in county_analysis[county_name]:
            county_analysis[county_name][candidate_name]={}
            # Adding keys and values to dic after initializing
            county_analysis[county_name][candidate_name]={"Candidate Votes":0,"Candidate Percentage":0}

        #if condition to check if the name already exists
        if candidate_name not in candidate_list:
            # if not, add it to the list of candidates.
            candidate_list.append(candidate_name)
            candidate_analysis[candidate_name]={}
            candidate_analysis[candidate_name]["Total Candidate Votes"]=0
        
        #Followindg set of codes is basically a incremental counter
        # The total numbers of votes each candidate won 
        candidate_analysis[candidate_name]["Total Candidate Votes"] += 1
        # The total numbers of votes each candidate won in 
        county_analysis[county_name][candidate_name]["Candidate Votes"] += 1
        # The total numbers of votes polled in couunty 
        county_analysis[county_name]["County Votes"] += 1
        
        # The percentage of votes each candidate won
        votes_percentage=candidate_analysis[candidate_name]["Total Candidate Votes"]/total_votes*100
        candidate_analysis[candidate_name]["Percentage"]=votes_percentage

#Open the file which stores the result of the analysis
with open(writefilepath,"w") as analysis_results_textfile:
    #Add ing the text to be written on file into a string
    election_results_summary = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    f"County Votes:\n"
    )
    #Write code to write sring to the file
    analysis_results_textfile.write(election_results_summary)
    print(election_results_summary)
    # Initializing variables to perform conditional analysis tp find winning candidate,votes and percentage
    winning_votes = 0
    winning_percentage = 0
    winning_candidate = " "
    # Initializing variables to perform conditional analysis tp find winning county,votes and percentage
    winning_county_votes = 0
    winning_county_percentage = 0
    winning_county_name = " "
    # Nested for loop to find out greatest votecount for county and candidate per county
    for county_name in county_list:
        # Percentage Calculation for county
            county_percentage=county_analysis[county_name]["County Votes"]/total_votes * 100
            county_analysis[county_name]["County Percentage"]=county_percentage
            county_summary=f'{county_name} county: {county_percentage:.1f}% ({county_analysis[county_name]["County Votes"]:,})\n'
            #Writing and printing county summary ie name votes and percentage
            analysis_results_textfile.write(county_summary)
            print(county_summary)
            print(f'\t* Vote Share Breakdown\n')

            #temp variable to store greater vote count to find greatest number of vote count
            temp_votes=0 
            county_winner_candidate=" "
            for candidate_name in candidate_list: 
                
                #Calculates percentage for county votes
                county_candidate_percentage=(county_analysis[county_name][candidate_name]["Candidate Votes"]/total_votes)*100
                county_analysis[county_name][candidate_name]["Candidate Percentage"]=county_candidate_percentage
                
                #Find leading candidate in a county and printing to screen in data facts later
                if county_analysis[county_name][candidate_name]["Candidate Votes"] > temp_votes:
                    temp_votes=county_analysis[county_name][candidate_name]["Candidate Votes"]
                    county_winner_candidate=candidate_name
                
                # The winner of the elections based on popular votes,counting total votes for a candidate
                if candidate_analysis[candidate_name]["Total Candidate Votes"] > winning_votes and candidate_analysis[candidate_name]["Percentage"] > winning_percentage:
                    winning_votes=candidate_analysis[candidate_name]["Total Candidate Votes"]
                    winning_percentage=candidate_analysis[candidate_name]["Percentage"]
                    winning_candidate=candidate_name
                
                print(f'\t\t--> {candidate_name}: {county_analysis[county_name][candidate_name]["Candidate Votes"]:,} votes\n')
               
            #Conditional statement to find largest county turnover
            if county_analysis[county_name]["County Votes"] > winning_county_votes and county_analysis[county_name]["County Percentage"] > winning_county_percentage:
                winning_county_votes=county_analysis[county_name]["County Votes"]
                winning_county_percentage=county_analysis[county_name]["County Percentage"]
                winning_county_name=county_name 

            ##Calculating and printing data facts about counties and candidates
            print(f'\t* Leading Candidate: {county_winner_candidate} with {temp_votes:,} votes. \n')
            print(f'\t* This is {temp_votes/county_analysis[county_name]["County Votes"]*100:.2f}% of total {county_name} county votes.\n')
            temp_percent=temp_votes/candidate_analysis[county_winner_candidate]["Total Candidate Votes"]*100
            print(f'\t* {temp_percent:.2f}% of total {county_winner_candidate} PyPoll votes were polled in {county_name} county. \n')
            
    # Addind larget turnover county name to string with formatting and text
    winning_county_summary=(
        f"-------------------------------\n"
        f"Largest County Turover : {winning_county_name}\n"
        f"-------------------------------\n"
    )
    #Printing and adding same to the file
    print(winning_county_summary)
    analysis_results_textfile.write(winning_county_summary)

    #For loop to print list of candidates who received votes
    # Note:This foor loop is added additionaly to match output.
    # Otherwise we can eliminate this loop and merge this code in same loop above
    for candidate_name in candidate_list:
        candidate_summary=f'{candidate_name}: {candidate_analysis[candidate_name]["Percentage"]:.1f}% ({candidate_analysis[candidate_name]["Total Candidate Votes"]:,})\n'
        analysis_results_textfile.write(candidate_summary)
        print(candidate_summary)

    #String to save winning candidate summary
    winning_candidate_summary=(
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_votes:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    #Printing and adding strind to the file
    print(winning_candidate_summary)
    analysis_results_textfile.write(winning_candidate_summary)

#last step:closing the files after performing operations
election_results_csvfile.close()
analysis_results_textfile.close()