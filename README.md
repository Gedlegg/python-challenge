# Python-Challenge
# Overview
    - Financial Analysis
    - Election Results Analysis
# Financial Analysis
    - Overview
        -This Python script analyzes financial data stored in a CSV file and prints out the results to the terminal. It also exports the results to a text file named PyBank_results.txt.
        
    - Script Details
        - The script initializes various variables to store financial data, such as total_months, net_total, previous_profit_loss, greatest_increase_date, greatest_increase_amount, greatest_decrease_date, greatest_decrease_amount, and total_changes.
        - It reads the data from the CSV file using Python's csv.reader module, skipping the header row.
        - The financial analysis is performed within a loop that iterates over each row of data in the CSV file.
        - Within the loop, the script calculates the total months, net total profit/loss, changes in profit/loss, greatest increase in profits, and greatest decrease in profits.
        - After processing all the data, the script calculates the average change in profit/loss.
        - The script prints the financial analysis results to the terminal, including total month, total, average change,greatest increase in profit, and greatest decrease in profit.
        - Finally, the script exports the election results to a text file named PyBank_results.txt located in the analysis folder. The text file contains the same information as printed in the terminal.
    
# Election Results Analysis
    - Overview
        - This Python script analyzes election data stored in a CSV file and prints out the results to the terminal. It also exports the results to a text file named PyPoll_results.txt.

    - Script Details
        - The script initializes various variables to store election data, such as total_votes,candidates, winner_name, and winner_votes.
        - It reads the data from the CSV file using Python's csv.reader module, skipping the header row.
        - The script counts the total number of votes cast and keeps track of the number of votes each candidate receives. It also determines the winner based on the candidate with the highest number of votes.
        - After counting the votes, the script calculates the percentage of votes each candidate received.
        - The script prints the election results to the terminal, including the total number of votes, the percentage of votes each candidate received, and the name of the winning candidate.
        - Finally, the script exports the election results to a text file named PyPoll_results.txt located in the analysis folder. The text file contains the same information as printed in the terminal.