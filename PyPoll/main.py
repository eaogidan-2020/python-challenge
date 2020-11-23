#Import Dependencies
import csv

#  Reference the file where the CSV is located, load and output
file_to_load = "Resources/election_data.csv"
file_to_output = "analysis/election_analysis_1.txt"


# Total vote for all condidate 
total_votes = 0

#Candidate Options list and candidate votes dictionary.
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count and percentage 
winning_candidate = ""
winning_count = 0

# convert csv to dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    # each row...
    for row in reader:        

        # Add a vote to that candidate's count
        total_votes = total_votes + 1

        # filterate candidate name 
        candidate_name = row["Candidate"]

        # if loop match candidate or not
        
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list. 
            candidate_options.append(candidate_name)

             # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
       
           
# Print out the results 
with open(file_to_output, "w") as txt_file:

    # Print out the final vote
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count 
    txt_file.write(election_results)

    # search for the winner in the counts
    for candidate in candidate_votes:

        # count/percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # compare vote count and winning candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # candidate's voter count/percentage 
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save your print
        txt_file.write(voter_output)

    # imprint the winning candidate 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save  print
    txt_file.write(winning_candidate_summary)