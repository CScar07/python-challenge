# Import dependencies
import os, csv
from pathlib import Path 

# Assign file location 
csvpath = os.path.join("election_data.csv")
# Declare Variables 
total_votes = 0 
Doane_votes = 0
Stockham_votes = 0
DeGette_votes = 0


# Open csv in default read mode with
with open(csvpath,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 
    header=next(csvreader)

   # print(header)
    

    for row in csvreader: 

        # Count the unique Voter ID's and store in variable  called total_votes
        total_votes +=1
       # print(row[2])
        # We have 3 candidates if the name is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements
        if row[2] == "Charles Casper Stockham":
            Stockham_votes += 1
        elif row[2] == "Diana DeGette":
            DeGette_votes += 1
        elif row[2] == "Raymon Anthony Doane": 
            Doane_votes += 1
        

 # To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["DeGette", "Doane", "Stockham"]
votes = [DeGette_votes, Doane_votes, Stockham_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
DeGette_percent = (DeGette_votes/total_votes) *100
Doane_percent = (Doane_votes/total_votes) * 100
Stockham_percent = (Stockham_votes/total_votes)* 100


# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"DeGette: {DeGette_percent:.3f}% ({DeGette_votes})")
print(f"Doane: {Doane_percent:.3f}% ({Doane_votes})")
print(f"Stockham: {Stockham_percent:.3f}% ({Stockham_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

output_file = Path("analysis")

with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Stockham: {Stockham_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Doane: {Doane_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"DeGette: {DeGette_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")

