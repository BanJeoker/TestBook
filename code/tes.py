text = "This is the content you want to save."

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(text)


for group_name, group_data in df.groupby('group'):
    print(f"Group {group_name}: {group_data['category'].tolist()}")
count_a = df.groupby('group')['category'].apply(lambda x: (x == 'a').sum())
