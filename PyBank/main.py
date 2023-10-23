#Import of necessary modules
import os
import csv

#CSV file path
budget_data = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#Create objects from CSV file
total_months = 0
total = 0
second_row = 0
first_row = 0
month_change = 0
total_month_change = []
date = []

#Open CSV reader 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
   
    #In each row, Read the header
    csv_header = next(csvreader)
   
    #Read data in each row after the header
    for row in csvreader:
    
        #Total number of months in dataset
        total_months += 1
        #Total amount of "Profit/Losses" over the entire period
        first_row = int(row[1])
        total += int(row[1])
        #Average of change in "Profit/Losses" over the entire period
        if (total_months==1):
            second_row = first_row
        else:
            month_change = first_row -second_row
            date.append(row[0])
            total_month_change.append(month_change)
            second_row = first_row
    average = round(sum(total_month_change)/(total_months -1), 2)

    # The greatest increase and decrease in profits (date and amount) over the entire period
    greatest_increase = max(total_month_change)
    greatest_decrease = min(total_month_change)
        
    increase_date = date[total_month_change.index(greatest_increase)]
    decrease_date = date[total_month_change.index(greatest_decrease)]

#Print analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {increase_date}(${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date}(${greatest_decrease})")

# Output Path and Export text file with analysis
output_path = os.path.join("..", "PyBank", "analysis", "Financial_Analysis_Summary.txt")

with open(output_path, 'w') as text:
    text.write(f"Financial Analysis\n")
    text.write(f"----------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${total}\n")
    text.write(f"Average Change: ${average}\n")
    text.write(f"Greatest Increase in Profits: {increase_date}(${greatest_increase})\n")
    text.write(f"Greatest Decrease in Profits: {decrease_date}(${greatest_decrease})")