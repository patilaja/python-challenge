"""
@Author: Ajay Patil
@Purpose: Read election_data file. Calculate total votes casted, votes received by the individual candidate, 
          % vote share of each candidate and declare the winner.
"""
# Import the os module and CSV files
import os
import csv

# Prepare CSV path
csvpath = os.path.join('', 'Resources', 'election_data.csv')
print("CSV Path",csvpath)

# Variable intialization
iKhan = 0
iCorry=0
iLi=0
iOTooley=0
iCounter=0
pKhan =0.00
pCorry=0.00
pLi=0.00
pOTooley=0.00
 
# Declaare a blank dictionary: this be populated with key as candidate name  and value as total votes for each candidate
dCandidates={}

# Read CSV file 
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
  
    # Read each row of data after the header and count votes received for individual candidate
    for row in csvreader:
        # Increment vote count
        iCounter=iCounter+1
        
        # Check who received the vote and add the vote in to the individual candidates vote count
        if(str(row[2])=="Khan"):
            iKhan=iKhan+1
        elif(str(row[2])=="Correy"):
            iCorry=iCorry+1
        elif(str(row[2])=="Li"):
            iLi=iLi+1
        elif(str(row[2])=="O'Tooley"):
            iOTooley=iOTooley+1
   
    # Calculate % votes received and format results to 3 decimal values
    pKhan ="{:.3f}".format(iKhan/iCounter*100)
    pCorry="{:.3f}".format(iCorry/iCounter*100)
    pLi="{:.3f}".format(iLi/iCounter*100)
    pOTooley="{:.3f}".format(iOTooley/iCounter*100)

    # Build dictionary of candidate and votes
    dCandidates ={"Khan":iKhan,"Corry":iCorry,"Li":iLi,"O'Tooley":iOTooley}

    # Get the winner name from the dictionay values who received highest votes: use of dictionary max function
    sWinner = max(dCandidates,key=dCandidates.get)

    # Print the results to the console
    print("") #optional added for console output spacing
    print("```text") 
    print("Election Results")
    print("-------------------------")     
    print("Total Votes: ", iCounter)
    print("-------------------------")    
    print(f"Khan: {pKhan}% ({iKhan})")
    print(f"Correy: {pCorry}% ({iCorry})")
    print(f"Li: {pLi}% ({iLi})")
    print(f"O'Tooley: {pOTooley}% ({iOTooley})")
    print("-------------------------")
    print(f"Winner: {sWinner}")
    print("-------------------------")
    print("```") 
    print("") #optional added for console output spacing

# Write output in to text file
with open("PyPollOutput.txt", "w") as text_file:

    # Write the block that was printed on the consol to file. Note: New line character \n is used to avoid writting each line one at a time.
    text_file.write(
        "```text\n"
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {iCounter}\n"
        "-------------------------\n"
        f"Khan: {pKhan}% ({iKhan})\n"
        f"Correy: {pCorry}% ({iCorry})\n"
        f"Li: {pLi}% ({iLi})\n"
        f"O'Tooley: {pOTooley}% ({iOTooley})\n"
        "-------------------------\n"
        f"Winner: {sWinner}\n"
        "-------------------------\n"
        "```")