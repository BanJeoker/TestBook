import pandas as pd

# Ensure the column is datetime
df['STATEMENTENDDATE'] = pd.to_datetime(df['STATEMENTENDDATE'])

# Extract month and day
month = df['STATEMENTENDDATE'].dt.month
day = df['STATEMENTENDDATE'].dt.day

# Define mask: within Dec 27–31 or Jan 1–5
mask = ((month == 12) & (day >= 27)) | ((month == 1) & (day <= 5))

# Keep only year-end rows
df_year_end = df[mask].copy()
