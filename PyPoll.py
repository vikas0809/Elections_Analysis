
# Add our dependencies.
import os
import csv
import datetime
import random
from sqlite3 import Row



# Set path for file
readfilepath=os.path.join('Resources','election_results.csv')
writefilepath=os.path.join('Resources','Elections Analysis.txt')

# Assign a variable to load a file from a path.
with open(readfilepath,"r") as election_results_csvfile:
    
    # Creating hadler for the file to perform read operations from csv file
    elections_data=csv.reader(election_results_csvfile,delimiter=",")

    header=next(elections_data)
    print(header)
    



# Assign a variable to save the file to a path.
with open(writefilepath,"w") as analysis_results_textfile:

    # Creating hadler for the file to perform write operations to file
    analysis_results=csv.reader(analysis_results_textfile)




election_results_csvfile.close()
analysis_results_textfile.close()
# The data we need to retreive.
# The totla number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total numbers of votes each candidate won
# The winner of the elections based on popular votes
