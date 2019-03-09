# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join( './PyPoll/Resources/', 'election_data.csv')
#print(csvpath)
print("\n Python Polls challenge \n")


## the write to txt file function
def printtxt(months,profit,avg,inc,incday,dec,decday):
    file = open("pollsresume.txt","w") 

    file.write(f"\nTotal months: {months}")
    file.close()



with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    total_votes=0
    candidates=[]
    candidates_votes=[]
    # Read each row of data after the header
    print("*** POLLS RESUME ****")
    for row in csvreader:
        total_votes+=1
        if row[2] in candidates:
            c=candidates.index(row[2])
            candidates_votes[c]=candidates_votes[c]+1
        else:
            candidates.append(row[2])
            candidates_votes.append(1)
    
    print(f"The total votes of the election: {total_votes:,}  ")
    winner=""
    winner_percentage=0.0
    c=0
    file = open("pollsresume.txt","w") 
    file.write("*** POLLS RESUME ****")
    
    for cand in candidates:
        percentage=candidates_votes[c]/total_votes*100
        print(f"Candidate: {cand} got {candidates_votes[c]:,} votes, and have the {percentage:,.2f}% of votes")
        file.write(f"\nCandidate: {cand} got {candidates_votes[c]:,} votes, and have the {percentage:,.2f}% of votes")
        if (percentage>winner_percentage):
            winner_percentage=percentage
            winner=cand
        c+=1
    file.write(f"\n\nThe winner of the election was: {winner} with {winner_percentage:,.2f}%")
    print(f"\n\nThe winner of the election was: {winner} with {winner_percentage:,.2f}%")
    file.close()
