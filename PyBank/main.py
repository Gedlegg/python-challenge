# importing dependency
import os
import csv

# Read the data from the file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0
total_change = 0

# Calculate total months, net total, changes, greatest increase, and greatest decrease
with open(csvpath) as csvfile: # Open the CSV file
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) # Skip the header row
    for i, row in enumerate(csvreader):
        total_months = total_months + 1
        current_profit_loss = int(row[1])
        net_total = net_total + current_profit_loss
        if i > 0:
            change = current_profit_loss - previous_profit_loss
            total_change = total_change + change
            if change > greatest_increase_amount:
                greatest_increase_amount = change
                greatest_increase_date = row[0]
            elif change < greatest_decrease_amount:
                greatest_decrease_amount = change
                greatest_decrease_date = row[0]
        previous_profit_loss = current_profit_loss

# Calculate average change
if total_months > 1:
    average_change = round((total_change / (total_months - 1)), 2)
else:
    average_change = 0

# Print results to the terminal
print(f"Financial Analysis\n------------------------ ")
print(f"Total Month: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")    

# Export results to the PyBank_results.txt
with open("analysis/PyBank_results.txt", "w") as file:
    file.write(f"Financial Analysis\n------------------------\n" )
    file.write(f"Total Month: {total_months} \n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")