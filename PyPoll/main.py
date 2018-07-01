# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV's
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
totalvote = 0
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    voteshare = {}
    for row in csvreader:
        if(row[2] in voteshare):
            voteshare[row[2]] += 1
        else:
            voteshare[row[2]]=  1
        totalvote +=1

outputfilepath = os.path.join('analysis', 'election_results.txt')
with open(outputfilepath, 'w') as outputfile:
    electionresults = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalvote}\n"
        f"-------------------------\n")
    print("\n")
    print(electionresults)
    outputfile.write(electionresults)
    winner = []  # list to hold name of winners. List is required in case of a tie
    maxvote = max(voteshare.values())   #variable to hold winning vote
    #print individual candidate result and write to file. 
    for candidate, vote in voteshare.items():
        candidateresult = (
            f"{candidate}: {(float(vote)/float(totalvote)*100):.3f}%  ({vote})\n")
        print(candidateresult)
        outputfile.write(candidateresult)
        #find the list of candidates who have maximum vote share
        if(vote == maxvote):
            winner.append(candidate)
    winnertext = (f"-------------------------\n")
    if(len(winner) == 1):
        winnertext = winnertext + (f"Winner: {winner[0]}\n"
               f"-------------------------\n")
    else:
        winnertext += "Tied election\nWinners are : "
        for i in range(0, len(winner)-1):
            winnertext += winner[i] + ", "
        winnertext += (f"and {winner[i+1]}\n-------------------------\n")
    outputfile.write(winnertext)
    print(winnertext)
    
    

