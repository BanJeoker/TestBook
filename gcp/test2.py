import pandas as pd
import glob
import os

# Provide the absolute path to the base folder where monthfolders are located
base_folder = 'C:/path_to_your_folder/'  # Replace with the full path to your folder

# Get a list of all monthfolders
month_folders = [f.path for f in os.scandir(base_folder) if f.is_dir()]

# Initialize an empty list to hold DataFrames
dataframes = []

# Iterate through each monthfolder
for month_folder in month_folders:
    # Find all Excel files in the current monthfolder
    excel_files = glob.glob(f"{month_folder}/*.xlsx")  # Adjust extension if needed
    
    # Filter out temporary files like '~$test.xlsx'
    excel_files = [file for file in excel_files if not os.path.basename(file).startswith('~$')]

    # Read each Excel file and append to the list of DataFrames
    for file in excel_files:
        df = pd.read_excel(file)
        dataframes.append(df)

# Concatenate all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Display the combined DataFrame
print(combined_df)

# Save the combined DataFrame to a new Excel file if needed
combined_df.to_excel('combined_output.xlsx', index=False)
