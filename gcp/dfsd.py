import pandas as pd

# Sample DataFrame
data = {'id': [1, 1, 2, 3, 3],
        'value': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

# Initialize an empty dictionary
result_dict = {}

# Iterate over each row
for index, row in df.iterrows():
    id_value = row['id']
    value = row['value']

    # If the ID is already in the dictionary, append the value to a list
    if id_value in result_dict:
        result_dict[id_value].append(value)
    # Otherwise, create a new list with the value
    else:
        result_dict[id_value] = [value]

print(result_dict)
