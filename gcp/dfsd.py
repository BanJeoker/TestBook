def sort_lists_by_timestamp(data_dict):
  """Sorts the inner lists of each key-value pair in the dictionary based on the timestamp.

  Args:
    data_dict: A dictionary where each key is a list of lists, and each inner list contains a double value and a timestamp.

  Returns:
    A new dictionary with the sorted inner lists.
  """

  sorted_dict = {}
  for key, value_list in data_dict.items():
    sorted_list = sorted(value_list, key=lambda x: x[1])  # Sort by the second element (timestamp)
    sorted_dict[key] = sorted_list
  return sorted_dict

# Example usage:
data = {
  "key1": [[1.2, "2023-11-22 12:34:56"], [3.4, "2023-11-21 09:12:34"], [2.5, "2023-11-23 18:00:00"]],
  "key2": [[5.6, "2023-12-01 10:00:00"], [4.7, "2023-11-30 15:30:00"]]
}

sorted_data = sort_lists_by_timestamp(data)
print(sorted_data)


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
