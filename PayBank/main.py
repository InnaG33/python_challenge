import os
import csv

# Path to collect data from the Resources folder
resources_path = os.path.join('..', '/Users/grinn/UCBWork/Python_Work/python_challenge/PayBank/Resources', 'budget_data.csv')

months = 0
net_total = 0
increase = 0
decrease = 10**9
daily_changes = []
date = []
net_daily_change = 0
daily_change = 0

# Open the CSV
with open(resources_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next (csvreader)

# Loop through to sum values
    for row in csvreader:
        months += 1
        net_total = net_total + int(row[1])
        daily_changes.append(float(row[1])-daily_change)
        daily_change = float(row[1])
        date.append(row[0])

# The greatest increase/decrease in profits (date and amount) over the entire period
for i in range(1, len(daily_changes)):
    net_daily_change = net_daily_change + daily_changes[i]

    if increase < daily_changes[i]:
        increase = int(daily_changes[i])
        increase_mon = date[i]
    if decrease > daily_changes[i]:
        decrease = int(daily_changes[i])
        decrease_mon = date[i]

net_daily_change = round(net_daily_change / (months-1), 2)

# Write results to CSV output file
output_path = os.path.join('..', '/Users/grinn/UCBWork/Python_Work/python_challenge/PayBank/output', 'output_budget_data.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =",")
    csvwriter.writerow(['Total months', months])
    csvwriter.writerow(['Total Loss/Profit', net_total])
    csvwriter.writerow(['Total Daily Change', net_daily_change])
    csvwriter.writerow(['Greatest Increase in Profits', increase_mon, increase])
    csvwriter.writerow(['Greatest Decrease in Profits', decrease_mon, decrease])

# Print results to terminal
print()
print("Financial Analysis")
print("---"*10)

print(f"Total months: {months}")
print(f"Total Loss/Profit: {net_total}")
#print(f"Total Average: {round(net_aver, 0)}")
print(f"Total Daily Change: {net_daily_change}")

print(f"Greatest Increase in Profits --> {increase_mon} : ${increase}")
print(f"Greatest Decrease in Profits --> {decrease_mon} : ${decrease}")

