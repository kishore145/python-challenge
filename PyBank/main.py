# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV's
import csv

#functiion to return the list by reading the input file. 
csvpath = os.path.join('Resources', 'budget_data.csv') # specifying relative location of budget data csv file
total = 0
monthcount = 0
lastmonthtot = 0
profit = 0
hightestprofit = []
hightestloss = []
monthlyprofit = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #seperate sequence of code for first row
    firstrow = next(csvreader)
    monthcount += 1
    total += int(firstrow[1])
    lastmonthtot = int(firstrow[1])
    monthlyprofit = [[firstrow[0],0.0]]
        
    #loopng through all remanng rows
    for row in csvreader:
        #calculates total months, total net, and each months profit
        monthcount += 1
        total += int(row[1])
        profit = int(row[1]) - lastmonthtot
        monthlyprofit.append([row[0],profit])
        lastmonthtot = int(row[1])

print("Financial Analysis \n----------------------------")
print("Total months : " + str(monthcount))
print("Total: $" + str(total))

#calculate highest profit and lowest profit and average.
netprofit = monthlyprofit[0][1]
hightestloss=monthlyprofit[0]
hightestprofit = monthlyprofit[0]

for i in range(1, monthcount):
    netprofit += monthlyprofit[i][1]
    if(monthlyprofit[i][1] < hightestloss[1] ):
        hightestloss = monthlyprofit[i]
        
    if(monthlyprofit[i][1] > hightestprofit[1] ):
        hightestprofit = monthlyprofit[i]


averageprofit = netprofit/(monthcount -1)
print("Average  Change: $" + format(averageprofit, '.2f'))
print("Greatest Increase in Profits: " + hightestprofit[0] + " ($" + str(hightestprofit[1]) + ")")
print("Greatest Decrease in Profits: " + hightestloss[0] + " ($" + str(hightestloss[1]) + ")")


# Write to file
file_write = os.path.join("analysis", "budget_analysis.txt")
# Export the results to text file
with open(file_write, "w") as txt_file:
    txt_file.write("Financial Analysis \n----------------------------")
    txt_file.write("\nTotal months : " + str(monthcount))
    txt_file.write("\nTotal: $" + str(total))
    txt_file.write("\nAverage  Change: $" + format(averageprofit, '.2f'))
    txt_file.write("\nGreatest Increase in Profits: " + hightestprofit[0] + " ($" + str(hightestprofit[1]) + ")")
    txt_file.write("\nGreatest Decrease in Profits: " + hightestloss[0] + " ($" + str(hightestloss[1]) + ")")

