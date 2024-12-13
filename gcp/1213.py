import pandas as pd

# Sample DataFrame
data = {
    'ID': [1, 2, 3, 2, 4, 5, 5],
    'Value': [10, 20, 15, 30, 25, 35, 40]
}
df = pd.DataFrame(data)

# Sort by 'Value' in descending order to prioritize highest values
df_sorted = df.sort_values(by='Value', ascending=False)

# Drop duplicates based on 'ID', keeping the first (highest value) occurrence
df_unique = df_sorted.drop_duplicates(subset='ID', keep='first')

# Select the top 2 rows with the highest values
top_2 = df_unique.head(2)

print(top_2)


for i, date in enumerate(dates):
    fig.add_annotation(
        x=date,
        y=values[i],
        text=date.strftime('%m/%d/%Y'),  # Format the date as a string
        showarrow=False,
        font=dict(size=10, color="black", angle=45),
        xanchor="center",
        yanchor="bottom",
        valign="bottom",  # Position the text above the points
        bgcolor="white"
    )



vertical_lines = pd.to_datetime(vertical_lines_str, format="%m/%d/%Y")

# Add vertical lines at each date in the list
for date in vertical_lines:
    fig.add_vline(x=date, line=dict(color="red", width=2, dash="dash"), name=f"Vertical Line {date.date()}")


fig.add_vline(x=3, line=dict(color="red", width=2, dash="dash"), name="Vertical Line")



import pandas as pd

# Sample DataFrame with datetime column
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'date': ['2024-01-01', '2024-05-15', '2024-03-01', '2024-12-01', '2024-06-20']
}
df = pd.DataFrame(data)

# Convert the 'date' column to datetime64
df['date'] = pd.to_datetime(df['date'])

# Define the specific day to compare
specific_day = '2024-06-01'

# Convert the specific day to datetime
specific_day = pd.to_datetime(specific_day)

# Filter rows where 'date' is larger than the specific day
filtered_df = df[df['date'] > specific_day]

print(filtered_df)
