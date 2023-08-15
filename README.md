# Financial Analysis Script README

## Overview

This Python script provides tools for analyzing financial data from two CSV files. The first dataset contains election results, while the second dataset consists of budget data. The goal of the script is to summarize the data and extract significant performance indicators.

## Features

### Election Analysis:

- **Reading the Dataset**: The script reads a CSV file containing election results.
- **Total Votes**: Computes the total number of votes cast in the election.
- **Candidates Overview**: Determines each candidate's total number of votes and their percentage of the total votes.
- **Winner Identification**: Identifies the candidate with the most votes and declares them the winner.
- **Results Export**: Outputs the results to a text file.

### Budget Analysis:

- **Reading the Dataset**: The script reads a CSV file containing budget data.
- **Total Months**: Computes the total number of months included in the dataset.
- **Net Total Amount**: Computes the net total amount of Profit/Losses over the entire period.
- **Average Changes**: Computes the average change in Profit/Losses over the entire period.
- **Greatest Increase**: Identifies the greatest increase in profits (date and amount) over the entire period.
- **Greatest Decrease**: Identifies the greatest decrease in losses (date and amount) over the entire period.
- **Results Export**: Outputs the results to a text file.

## How to Use

1. **Setup**: 
   - Ensure the script is in the same directory as the `Resources` folder, which should contain `election_data.csv` and `budget_data.csv`.
   - The script will output results to an `Analysis` folder, creating a `Results.txt` file within.
2. **Run the Script**: 
   - Execute the script using Python.
   - The script will process each dataset in turn, print the analysis results to the console, and save the results to `Results.txt`.
3. **View Results**:
   - Open the `Results.txt` file in the `Analysis` folder to view the summarized data.

## Requirements

- Python 3.x
- CSV files: `election_data.csv` and `budget_data.csv` located in the `Resources` directory.

## Notes

- It's essential to ensure the structure and contents of the CSV files match the expected format. Any changes to the file structure or format may lead to errors or incorrect calculations.
- The script will overwrite the `Results.txt` file if it already exists in the `Analysis` folder.

## Feedback & Contributions

Please report any issues or suggest improvements. Contributions to enhance the functionality or address bugs are always welcome!
