from google.cloud import storage

def check_and_create_folder(bucket_name, folder_path):
    # Initialize the GCS client
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    
    # Ensure folder path ends with '/'
    if not folder_path.endswith('/'):
        folder_path += '/'
    
    # Check if folder exists
    blobs = list(client.list_blobs(bucket, prefix=folder_path, max_results=1))
    if blobs:
        print(f"Folder '{folder_path}' already exists in bucket '{bucket_name}'.")
    else:
        # Create a placeholder object to simulate folder creation
        blob = bucket.blob(folder_path)  # This is the "folder"
        blob.upload_from_string('')  # Empty string as content
        print(f"Folder '{folder_path}' created in bucket '{bucket_name}'.")

# Example usage
bucket_name = "your-bucket-name"
folder_path = "your-folder-path"

check_and_create_folder(bucket_name, folder_path)


import pandas as pd

# Original DataFrame with text-based IDs and made-up date strings for even columns
data_with_text_ids = {
    "id1": ["A1", "B1", "C1", "D1", "E1"],
    "2023-01-01": [10, 20, 30, 40, 50],
    "id2": ["A2", "B2", "C2", "D2", "E2"],
    "2023-02-01": [15, 25, 35, 45, 55],
    "id3": ["A3", "B3", "C3", "D3", "E3"],
    "2023-03-01": [12, 22, 32, 42, 52],
    "id4": ["A4", "B4", "C4", "D4", "E4"],
    "2023-04-01": [18, 28, 38, 48, 58],
    "id5": ["A5", "B5", "C5", "D5", "E5"],
    "2023-05-01": [14, 24, 34, 44, 54]
}

# Create the DataFrame
df = pd.DataFrame(data_with_text_ids)

# Initialize an empty dictionary to store the results
result_dict_text = {}

# Iterate through each row and extract the pairs
for index, row in df.iterrows():
    # Loop through pairs of (id, data) columns
    for i in range(0, len(df.columns), 2):
        key = row[df.columns[i]]  # Odd columns are the keys (ID)
        value = str(row[df.columns[i+1]])  # Convert the data value to string
        column_name = df.columns[i+1]  # Column name for data

        # Check if the key already exists in the dictionary
        if key not in result_dict_text:
            result_dict_text[key] = []

        # Append the value + column name (date string) to the list of the corresponding key
        result_dict_text[key].append(value + column_name)

# Display the resulting dictionary with text-based IDs and date-based column names
result_dict_text
