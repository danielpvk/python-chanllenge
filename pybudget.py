# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join( './PyBank/Resources/', 'budget_data.csv')
#print(csvpath)
print("\n Python budget challenge \n")
def printtxt(months,profit,avg,inc,incday,dec,decday):
    file = open("budgetresume.txt","w") 

    file.write(f"\nTotal months: {months}")
    file.write(f"\nNet Profit/loss: ${profit:,}")
    file.write(f"\nAverage changes: ${avg:,.2f}")
    file.write(f"\nThe greatest increast of profits was the {incday} and the amount was ${inc:,}")
    file.write(f"\nThe greatest decreast of profits was the {decday} and the amount was ${dec:,}")
    file.close()

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
  #  print(f"CSV Header: {csv_header}")

    total_months=0
    net_profit_loss=0
    greatest_increase=0
    greatest_decrease=0
    last_day_profit=0
    avg_increase=0
    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
        net_profit_loss = net_profit_loss + int(row[1])
        increase=int(row[1])-last_day_profit
        #decrease=last_day_profit-int(row[1])
        avg_increase=avg_increase+increase
        if (increase>greatest_increase):
            greatest_increase = increase
            day_greatest_increase = row[0]
        if (increase<greatest_decrease):
            greatest_decrease = increase
            day_greatest_decrease = row[0]
        
    
    print(f"Total months: {total_months}")
    print(f"Net Profit/loss: ${net_profit_loss:,}")

    
  # The average of the changes in "Profit/Losses" over the entire period
    avg_increase=avg_increase/total_months
    print(f"Average changes: ${avg_increase:,.2f}")

  # The greatest increase in profits (date and amount) over the entire period
    print(f"The greatest increast of profits was the {day_greatest_increase} and the amount was ${greatest_increase:,}")
    
    print(f"The greatest decreast of profits was the {day_greatest_decrease} and the amount was ${greatest_decrease:,}")
    printtxt(total_months,net_profit_loss,avg_increase,greatest_increase,day_greatest_increase,greatest_decrease,day_greatest_decrease)

