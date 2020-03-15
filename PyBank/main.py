"""
@Author: Ajay Patil
@Purpose: Read budget_data data file and calculate total months, net total amount and average of changes to profit/loss, 
          greatest increase in profits, greateste decrease in losses over the period of time. 
          Using list, dictionary abd related functions to calculate min and max values rather than using loops. 
"""
# Import the os module and CSV files
import os
import csv

# Prepare CSV path
csvpath = os.path.join('', 'Resources', 'budget_data.csv')
print("CSV Path",csvpath)

# Variable intialization
iProfitLoss=0
iCounter=0
iMonths = 0
iTotal=0
iAverageChange=0
iGreatestIncrease=0
iGreatestDecrease=0
sMonthIncrease =""
sMonthDecrease =""
 
# Declare a blank list - this will be used to store profit/loss values from the column B
lProfitLoss =[]

# Declare a blank dictionary - this will be used to store months from column A and calculated cummulative value 
dCummulative={}

# Read CSV file 
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first  
    csv_header = next(csvreader)
    
    # Read each row of data after the header and count months, calculate cummulative values  
    for row in csvreader:

        # Beginning of the file - set first cummulative value as same value as profit/loss
        if iCounter==0:
            iCummuValue=row[1]
        else:   
            # Calculate cummulative value: this is profit/loss value of a current row - profit/loss value of previous row
            iCummuValue = int(row[1]) - int(iProfitLoss)
        
        # Lets build profit/loss list: Converting excel row cell value to integer to build a list that will hold integer values
        lProfitLoss.append(int(row[1]))

        # Increment counter value - this is used to count # of months 
        iCounter=iCounter+1
        
        # Build total profit/loss value: add current row value to current total profit/loss value
        iTotal = iTotal + int(row[1])

        # Store row profit/loss value - it will override once used to calulate cummulative value for the next row
        iProfitLoss = row[1]
        
        # Lets build dictionary: key as a month and value as cummulative profit/loss
        dCummulative.update({str(row[0]) : int(iCummuValue)}) 

    # Get greatest increase in profit/loss: use of dictionary max fuction
    iGreatestIncrease = max(dCummulative.values())

    # Get gretest decrease in profit/loss: use of dictionary min function
    iGreatestDecrease = min(dCummulative.values())

    # Get month of greatest increase in profit/loss
    sMonthIncrease = max(dCummulative, key=dCummulative.get) 

    # Get month of greatest decrease in profit/loss
    sMonthDecrease = min(dCummulative, key=dCummulative.get)

    # Calculate avaerage change and round to the two decimal place value
    iAverageChange = round((int((lProfitLoss[len(lProfitLoss)-1])) -int(lProfitLoss[0]))/(iCounter-1),2)

    # Print Results
    print("")
    print("```text")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {iCounter}")
    print(f"Total: ${iTotal}")
    print(f"Average  Change: ${iAverageChange}")
    print(f"Greatest Increase in Profits: {sMonthIncrease} (${iGreatestIncrease})")
    print(f"Greatest Decrease in Profits: {sMonthDecrease} (${iGreatestDecrease})")
    print("```")

# Write output in to text file
with open("PyBankOutput.txt", "w") as text_file:
    # Write the block that was printed on the consol to file. Note: New line character \n is used to avoid writting each line one at a time.
    text_file.write(
        "```text\n"
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {iCounter}\n"
        f"Total: ${iTotal}\n"
        f"Average  Change: ${iAverageChange}\n"
        f"Greatest Increase in Profits: {sMonthIncrease} (${iGreatestIncrease})\n"
        f"Greatest Decrease in Profits: {sMonthDecrease} (${iGreatestDecrease})\n"
        "```")