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



'''
Refined Analogy with Multiple Indices and Keys Example
Index (the “door”): The index is like a door that stores specific data you want to access. Each door can serve a unique purpose or dataset (e.g., different embeddings, model versions, or data sources). Importantly, one door (index) can have multiple keys (deployed indices), allowing it to be accessed in different ways or used for different purposes.

Index Endpoint (the “key ring”): The index endpoint acts like a key ring that holds multiple keys, each configured to open specific doors. By adding a deployed index, you effectively add a key to the key ring, allowing access to a particular index. This structure enables the endpoint to manage multiple keys for different indices or even multiple keys for the same index.

Deployed Index (the “key” that unlocks a specific door): Each deployed index is a key configured to open a specific door. When you create a deployed index, it’s like adding a uniquely labeled key to the endpoint’s key ring, allowing it to access the correct index. The deployed index ID serves as the unique identifier for each key, so the endpoint knows exactly which key to use for each query. This setup allows the same index to be accessed with multiple keys if needed, supporting flexibility and different use cases.


'''

from IPython.display import Image, display

# Display a local image
display(Image(filename='keychain_no_keys.png'))

import matplotlib.pyplot as plt

# Your list of numbers
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create the histogram
plt.hist(numbers, bins=5, edgecolor='black')  # `bins` specifies the number of bins
plt.title('Histogram of Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()
