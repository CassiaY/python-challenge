#importing modules
import os
import csv

#reading csv file, storing header row
csv_path = os.path.join("PyPoll", "Resources", "election_data.csv")
with open(csv_path) as csv_file:
    csvreader=csv.reader(csv_file, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)

    #creating empty lists
    voter_ID = []
    candidates_list = []
    county_list = []
    cand1 = []
    cand2 = []
    cand3 = []

    #appending items from csv to empty lists
    for row in csvreader:
        voter_ID.append(row[0])
        county_list.append(row[1])
        candidates_list.append(row[2])
        
    #calculations

    for x in candidates_list:
        if x == "Charles Casper Stockham":
            cand1.append(x)
            cand1_tot = len(cand1)
        elif x == "Diana DeGette":
            cand2.append(x)
            cand2_tot = len(cand2)
        elif x == "Raymon Anthony Doane":
            cand3.append(x)
            cand3_tot = len(cand3)

    print(f'c1tot: {cand1_tot}')
    print(f'c2tot: {cand2_tot}')
    print(f'c3tot: {cand3_tot}')

    total_votes = len(list(voter_ID))
    cand1_percent = round(cand1_tot/total_votes*100,2)
    cand2_percent = round(cand2_tot/total_votes*100,2)
    cand3_percent = round(cand3_tot/total_votes*100,2)

    print(f'c1p: {cand1_percent}')
    print(f'c2p: {cand2_percent}')
    print(f'c3p: {cand3_percent}')

    #determining winner
    if cand1_tot > cand2_tot and cand1_tot > cand3_tot:
        winner = "Charles Casper Stockham"
    elif cand2_tot > cand1_tot and cand2_tot > cand3_tot:
        winner = "Diana DeGette"
    elif cand3_tot > cand1_tot and cand3_tot > cand2_tot:
        winner = "Raymon Anthony Doane"

    #printing results in the terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes:  {total_votes}")
    print("----------------------------")
    print(f"Charles Casper Stockham:  {cand1_percent}% ({cand1_tot})")
    print(f"Diana DeGette:  {cand2_percent}% ({cand2_tot})")
    print(f"Raymon Anthony Doane:  {cand3_percent}% ({cand3_tot})")
    print("----------------------------")
    print(f"Winner:  {winner}")
    print("----------------------------")

    #Exporting results to a text file:
    output_path = os.path.join("PyPoll/analysis/PyPoll_output.txt")
    with open(output_path, 'w') as text:
        text.write("Election Results\n")
        text.write("----------------------------\n")
        text.write(f"Total Votes:  {total_votes}\n")
        text.write("----------------------------\n")
        text.write(f"Charles Casper Stockham:  {cand1_percent} ({cand1_tot})\n")
        text.write(f"Diana DeGette:  {cand2_percent} ({cand2_tot})\n")
        text.write(f"Raymon Anthony Doane:  {cand3_percent} ({cand3_tot})\n")
        text.write("----------------------------\n")
        text.write(f"Winner:  {winner}\n")
        text.write("----------------------------\n")
