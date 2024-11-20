from google.cloud import storage

# Initialize the GCS client
client = storage.Client()

# Define the bucket name and folder name
bucket_name = "your-bucket-name"
folder_name = "your-folder-name/"  # Add a trailing slash to indicate a folder

# Get the bucket
bucket = client.bucket(bucket_name)

# Create a "dummy" blob to represent the folder
blob = bucket.blob(folder_name)
blob.upload_from_string('')  # Upload an empty string as the content

print(f"Folder '{folder_name}' created in bucket '{bucket_name}'.")
