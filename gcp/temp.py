# Original nested dictionary structure
data = {
    "item_group_1": {
        "item1": {"a": 1, "b": 2, "c": 3},
        "item2": {"a": 4, "b": 5, "c": 6},
        "item3": {"a": 7, "b": 8, "c": 9},
    },
    "item_group_2": {
        "item1": {"a": 10, "b": 20, "c": 30},
        "item2": {"a": 40, "b": 50, "c": 60},
        "item3": {"a": 70, "b": 80, "c": 90},
    },
}

# List of keys to keep in 'temp_dict'
keys_to_keep = ["a", "c"]

# Filtering logic
filtered_data = {
    group: {
        item: {k: v for k, v in temp_dict.items() if k in keys_to_keep}
        for item, temp_dict in items.items()
    }
    for group, items in data.items()
}

# Result
print(filtered_data)



# Original list of dictionaries
list_of_dicts = [
    {"item1": {"a": 1, "b": 2, "c": 3}},
    {"item2": {"a": 4, "b": 5, "c": 6}},
    {"item3": {"a": 7, "b": 8, "c": 9}},
]

# List of keys to keep in 'temp_dict'
keys_to_keep = ["a", "c"]

# Filtering logic
filtered_list = [
    {outer_key: {k: v for k, v in temp_dict.items() if k in keys_to_keep}}
    for d in list_of_dicts
    for outer_key, temp_dict in d.items()
]

# Result
print(filtered_list)
