for group_name, group_data in df.groupby('group'):
    print(f"Group {group_name}: {group_data['category'].tolist()}")
