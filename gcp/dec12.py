import pandas as pd

# Sample DataFrame
data = {
    'timestamp': ['2024-01-01', '2024-05-15', '2024-12-01'],
    'value': [10, 20, 30]
}
df = pd.DataFrame(data)

# Convert the timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Define the specific day
specific_date = '2024-06-01'

# Filter rows where timestamp is after the specific date
filtered_df = df[df['timestamp'] > specific_date]

print(filtered_df)
