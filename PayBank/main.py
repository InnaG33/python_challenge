import os
import csv
import math

# Path to collect data from the Resources folder
resources_path = os.path.join('..', '/Users/grinn/UCBWork/Python_Project/PayBank/Resources', 'budget_data.csv')

months = 0
net_total = 0
increase = 0
decrease = 10**9
sq_net_aver_change = 0
net_aver_change = 0

# Open the CSV
with open(resources_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)

    # Loop through to sum values
    for row in csvreader:
#       decease = row[1]
        months += 1
        net_total = net_total + int(row[1])

# The greatest increase/decrease in profits (date and amount) over the entire period
        if increase < int(row[1]):
            increase = int(row [1])
            increase_mon = row[0]
        if decrease > int(row[1]):
            decrease = int(row [1])
            decrease_mon = row[0]

# The average of the changes in "Profit/Losses" over the entire period   
net_aver = int(net_total / months)

with open(resources_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)
    
    for row in csvreader:
        net_aver_change = net_aver_change + (int(row[1])-net_aver)

#round(net_aver_change, 2)
#net_aver_change = sq_net_aver_change

print()
print("Financial Analysis")
print("--"*10)

print(f"Total month: {months}")
print(f"Total Loss/Profit: {net_total}")
print(f"Total Average: {net_aver}")
print(f"Total Change in Average: {net_aver_change}")

print(f"Greatest Increase: {increase_mon} --> ${increase}")
print(f"Greatest Decrease: {decrease_mon} --> ${decrease}")

