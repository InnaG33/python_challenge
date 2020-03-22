import os
import csv

# # Path to collect data from the Resources folder (please update the folderpath, if needed)
resources_path = os.path.join('..', '/Users/grinn/UCBWork/Python_Work/python_challenge/PayPoll/Resources', 'election_data.csv')

candidates = []
votes_count = []

# Open the CSV to list data from candidates column 
with open(resources_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)

    for row in csvreader:  
        candidates.append(str(row[2]))

# creating a dictionary with candidates as keys, and their votes_count as values     
candidates_count = {}
for candidate in candidates:
    if candidate in candidates_count:
        candidates_count[candidate] += 1
    else:
        candidates_count[candidate] = 1

# extracting candidates and their votes_count from the dictionary
votes_str = []
names = []
for key in candidates_count.keys():
    votes_str.append(candidates_count[key])
    names.append(str(key))

votes = []
for vote in votes_str:
    votes.append(int(vote))
total_votes = sum(votes)

# percent votes from the total
votes_percent = []
for vote in votes:
    votes_percent.append(round(vote / total_votes * 100, 3))

max_percent = max(votes_percent)
min_percent = min(votes_percent)

# who is the winner 
for i in range(len(votes_percent)):
    if votes_percent[i] == max_percent:
        winner = names[i]
        winner_votes = int(votes[i])
    # if votes_percent[i] == min_percent:
    #     looser = names[i]
    #     looser_votes = int(votes[i])

# Print results to terminal
print()
print("Election Results")
print("--"*20)
print("Total Votes: " , total_votes)
print("--"*20)
for i in range(len(names)):
    print(f"{names[i]}: {votes_percent[i]}%  ({votes[i]})")

print("--"*20)
print("Winner: ", winner)
print("--"*20)

# Write results to CSV output file
output_path = os.path.join('..', '/Users/grinn/UCBWork/Python_Work/python_challenge/PayPoll/output', 'output_election_data.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =",")
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes:', total_votes])
    csvwriter.writerow([])
    for i in range(len(names)):
        csvwriter.writerow([names[i], str(votes_percent[i])+'%', votes[i]])
    
    csvwriter.writerow(["Winner: ", winner])
