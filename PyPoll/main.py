#specify the column header row and the item delimiter
import csv

# load file and output it
file_to_load = "Resources/election_data.csv"
file_to_output = "analysis/election_analysis_1.txt"

# sum of all Vote 
total_votes = 0

# Vote Counters/option for the candidates
candidate_options = []
candidate_votes = {}

# Winning and Count Tracker for candidate
winning_candidate = ""
winning_count = 0

# convert csv into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    # each row...
    for row in reader:        

        # total vote count + 1
        total_votes = total_votes + 1

        # filter the candidate name 
        candidate_name = row["Candidate"]

        # check if loop match existing candidate candidate or not
        
        if candidate_name not in candidate_options:

            # apply it to the list of running candidates 
            candidate_options.append(candidate_name)

            # start tracking the voter count of candidate
            candidate_votes[candidate_name] = 0

        # add 1 vote 
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    
# Print out the results 
with open(file_to_output, "w") as txt_file:

    # Print the final vote
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count 
    txt_file.write(election_results)

    # loop through the counts for the winner
    for candidate in candidate_votes:

        # find vote count/percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # analyse vote count and winning candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's voter count/percentage 
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save your print
        txt_file.write(voter_output)

    # Print the winning candidate 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save your print
    txt_file.write(winning_candidate_summary)