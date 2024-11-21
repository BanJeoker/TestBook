import pandas as pd
import glob

# Define the folder path where the Excel files are stored
folder_path = 'path_to_your_folder/'  # Replace with your folder path

# Get a list of all Excel files in the folder
excel_files = glob.glob(f"{folder_path}/*.xlsx")  # Adjust extension if needed (e.g., .xls)

# Read and append all Excel files into a single DataFrame
dataframes = []
for file in excel_files:
    df = pd.read_excel(file)  # Read each Excel file
    dataframes.append(df)

# Concatenate all DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Display the combined DataFrame
print(combined_df)

# Save the combined DataFrame to a new Excel file if needed
combined_df.to_excel('combined_output.xlsx', index=False)
