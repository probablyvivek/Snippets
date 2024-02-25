import pandas as pd
import os

# Directory where your sales data CSV files are stored
directory = "./Programming/Snippets/Sales/"

# List all CSV files in the directory
files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Initialize an empty DataFrame to store all combined data
all_months_data = pd.DataFrame()

# Loop through each file, read it into a DataFrame, and append it to the all_months_data DataFrame
for file in files:
    df = pd.read_csv(directory + file)
    all_months_data = pd.concat([all_months_data, df])

# Reset the index of the final DataFrame
all_months_data.reset_index(drop=True, inplace=True)

# Save the combined DataFrame to a new CSV file
all_months_data.to_csv(directory + "Final_Sales.csv", index=False)

print("Files combined successfully!")
