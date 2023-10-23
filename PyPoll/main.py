#Import of necessary modules
import os
import csv

#csv file path
election_data = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

#Variables to capture from csv file
totalvotes = 0
candidates =[]
number_votes =[]
candidates_percent_votes = []

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    #In each row, Read the header
    csv_header = next(csvreader)

    #Read data in each row after the header
    for row in csvreader:
        #Total Votes Cast
        totalvotes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1
    
    #Percentage of Votes Per Candidates
    for votes in number_votes:
        percentage = (votes/totalvotes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        candidates_percent_votes.append(percentage)
    
    # Election Winner based on popular vote
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]

# Print Election Results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(totalvotes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(candidates_percent_votes[i])} ({str(number_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Output Path and Export text file with analysis
output_path = os.path.join("..", "PyPoll", "analysis", "Election Results.txt")

with open(output_path, 'w') as text:
    text.write(f"Election Results\n")
    text.write(f"--------------------------\n")
    text.write(str(f"Total Votes: {str(totalvotes)}\n"))
    text.write(f"--------------------------\n")
    for i in range(len(candidates)):
        text.write(str(f"{candidates[i]}: {str(candidates_percent_votes[i])} ({str(number_votes[i])})\n"))
    text.write(f"--------------------------\n")
    text.write(str(f"Winner: {winning_candidate}\n"))
    text.write(f"--------------------------\n")