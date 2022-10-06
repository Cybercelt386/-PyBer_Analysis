#add dependencies 

import csv
import os

fileToLoad = os.path.join('resources', 'election_results.csv')

# create a filename variable to a direct or indirect path to the file.
fileToSave = os.path.join('analysis','election_analysis.txt') #this is the file location

Total_votes = 0 

caniditeOptions = []

canidite_Votes = {}

winningCanidite = ""

winningCount = 0

winningPercent = 0

# use with statement to open a txt file.
with open(fileToSave,'w') as txt_file:
    txt_file.write("Is mise Alasdair. Cad is ainm duit?")

#use the open statement to open the file as a txt file.

outfile = open(fileToSave, 'w')                # This file wil over write the previous entry both are saved to fileToSave with 
outfile.write("Counties in the election")      # election_analysis.txt as the extention
outfile.write("\n-------------------------------------------")

# write 3 counties into file.
outfile.write("\n Arapahoe,")
outfile.write("\n Denver,")
outfile.write("\n Jefferson")

#close the file
outfile.close

#perform analysis
fileToLoad = os.path.join('resources', 'election_results.csv')

with open(fileToLoad) as election_data:
    #Read the file object with the reader function
    fileReader = csv.reader(election_data)
    
    #print the header row
    headers = next(fileReader)
     
    #Print each row in the CSV file.
    for row in fileReader:
        Total_votes +=1

        caniditeName = row [2]

        #if the canadite does not match any exiting canadite add it to the list
        if caniditeName not in caniditeOptions:

            caniditeOptions.append(caniditeName)

            # track canidites voter count
            canidite_Votes[caniditeName] = 0

        canidite_Votes[caniditeName]+=1

        votes = canidite_Votes[caniditeName]

        votesPercenatge = float(votes) / float(Total_votes) * 100

        #print each canidite, their voter count, and percentage.
        print(f"{caniditeName}: {votesPercenatge:1f}% ({votes:,}))\n")

        # Save the results to our text file.
with open(fileToSave, "w") as txt_file:


    # After opening the file print the final vote count to the terminal.
    election_results = (

        f"\nElection Results\n"

        f"-------------------------\n"

        f"Total Votes: {Total_votes:,}\n"

        f"-------------------------\n")

    print(election_results, end="")

    # After printing the final vote count 
    # to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in canidite_Votes:


        # Retrieve vote count and percentage.
        votes = canidite_Votes[candidate_name]

        vote_percentage = float(votes) / float(Total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        
        #determine the winning vote
        if (votes > winningCount) and (votesPercenatge > winningPercent):

            winningCount = votes

            winningCanidite = caniditeName

            winningPercent = votesPercenatge

        WinningCaniditeSummery = (
            f"-----------------------------\n"

            f"Winner: {winningCanidite} \n"

            f"winning vote count: {winningCount}\n"

            f"Winning percentage {winningPercent:.1f}%\n"

            f"-----------------------------\n"

        )    
        
        print(WinningCaniditeSummery)

    # Save the winning candidate's results to the text file.
    txt_file.write(WinningCaniditeSummery)
