vertical_lines = [
    pd.to_datetime("2024-01-02"),
    pd.to_datetime("2024-01-04")
]

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
