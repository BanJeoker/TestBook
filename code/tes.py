from google.cloud import storage

# Initialize the GCP storage client
client = storage.Client()

# Set the name of the source and destination buckets
source_bucket_name = 'your-source-bucket'
destination_bucket_name = 'your-destination-bucket'

# Get the source and destination bucket objects
source_bucket = client.get_bucket(source_bucket_name)
destination_bucket = client.get_bucket(destination_bucket_name)

# Specify the root folder inside the source bucket
root_folder = 'your-root-folder/'  # The root folder within the source bucket

# List all objects (files/folders) within the root folder
blobs = source_bucket.list_blobs(prefix=root_folder)

# Iterate over each blob (file or folder)
for blob in blobs:
    # We are only interested in files, not folders
    if blob.name.endswith('.json'):  # You can adjust this condition if needed
        # Define the destination blob (object) name in the destination bucket
        destination_blob = destination_bucket.blob(blob.name)

        # Copy the file from the source bucket to the destination bucket
        destination_blob.copy_from(blob)
        print(f"Copied {blob.name} from {source_bucket_name} to {destination_bucket_name}")



from google.cloud import storage
import os

# Initialize the GCP storage client
client = storage.Client()

# Set the path to your root folder containing subfolders
root_folder = '/path/to/your/root/folder'
bucket_name = 'your-destination-bucket'

# Get the bucket object
bucket = client.get_bucket(bucket_name)

# Iterate through each subfolder in the root folder
for subfolder in os.listdir(root_folder):
    subfolder_path = os.path.join(root_folder, subfolder)

    # Check if it's a folder (not a file)
    if os.path.isdir(subfolder_path):
        # Iterate over the files inside the subfolder
        for file_name in os.listdir(subfolder_path):
            local_file = os.path.join(subfolder_path, file_name)

            # Check if it's a JSON file
            if os.path.isfile(local_file) and file_name.endswith('.json'):
                # Define the destination blob (object) name
                blob = bucket.blob(f"{subfolder}/{file_name}")

                # Upload the file to the bucket
                blob.upload_from_filename(local_file)
                print(f"Copied {file_name} from {subfolder} to {bucket_name}")



import os
import subprocess

# Set the path to your local folder and the GCP bucket URI
local_folder = '/path/to/your/folder'
bucket_uri = 'gs://your-bucket-name/'

# Iterate over each file in the local folder
for file_name in os.listdir(local_folder):
    local_file = os.path.join(local_folder, file_name)
    
    # Check if it's a file (not a subdirectory)
    if os.path.isfile(local_file):
        # Construct the gsutil cp command
        command = f"gsutil cp {local_file} {bucket_uri}"
        
        # Execute the command
        subprocess.run(command, shell=True, check=True)
        print(f"Copied {file_name} to {bucket_uri}")



for col in df.select_dtypes(include=[np.float64]).columns:
    df[col] = df[col].astype(object).map(float)

df.loc[df['type'].str.contains('value change', na=False), df.columns != 'type'] = \
    df.loc[df['type'].str.contains('value change', na=False), df.columns != 'type'].applymap(format_value)


import pandas as pd

# Sample DataFrame
data = {
    'A': [1.5, -2.3, 0, 4.2],
    'B': [-3.4, 0, 2.1, -1.1],
    'C': ['text', 5, 0.0, -2.7]  # Mixed column
}

df = pd.DataFrame(data)

# Function to convert float values
def format_value(value):
    if isinstance(value, float):  # Check if it's a float
        if value > 0:
            return f"an increase of {abs(value)}"
        elif value < 0:
            return f"a decrease of {abs(value)}"
        else:
            return "remain unchanged at 0"
    return value  # Keep non-float values unchanged

# Apply function to all values in the DataFrame
df = df.applymap(format_value)

# Display the updated DataFrame
import ace_tools as tools
tools.display_dataframe_to_user(name="Formatted DataFrame", dataframe=df)



import nbconvert

exporter = nbconvert.HTMLExporter()
body, resources = exporter.from_filename("your_notebook.ipynb")

with open("your_notebook.html", "w", encoding="utf-8") as f:
    f.write(body)



import nbformat
from nbconvert import HTMLExporter

# Load the notebook
with open("your_notebook.ipynb") as f:
    notebook = nbformat.read(f, as_version=4)

# Remove input cells
for cell in notebook.cells:
    if cell.cell_type == "code":
        cell.source = ""  # Remove code content

# Convert to HTML
exporter = HTMLExporter()
body, resources = exporter.from_notebook_node(notebook)

# Save the HTML output
with open("your_notebook.html", "w", encoding="utf-8") as f:
    f.write(body)

