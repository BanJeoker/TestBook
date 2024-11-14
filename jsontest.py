import json

# Load the JSON data from the file
with open('file.json', 'r') as f:
    data = f.read()

# Remove extra blank lines (lines that are just spaces or empty)
cleaned_data = "\n".join([line for line in data.splitlines() if line.strip()])

# Load the cleaned data into a JSON object
json_data = json.loads(cleaned_data)

# Save the cleaned JSON back to the file
with open('file.json', 'w') as f:
    json.dump(json_data, f, indent=4)
