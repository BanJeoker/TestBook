import pandas as pd

# Sample DataFrame
data = {
    'name': ['doc1', 'doc1', 'doc1', 'doc2', 'doc2', 'doc2'],
    'num_words': [100, 150, 200, 120, 180, 250],
    'section': ['Section1', 'Section2', 'Section3', 'Section1', 'Section2', 'Section3']
}

df = pd.DataFrame(data)

# Pivot the DataFrame to get num_words for each section in a single row
pivot_df = df.pivot(index='name', columns='section', values='num_words').reset_index()

# Calculate the correlation between Section1 and Section2
correlation = pivot_df['Section1'].corr(pivot_df['Section2'])

print(f"Correlation between num_words in Section1 and Section2: {correlation:.2f}")


from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Print the current date and time in a specific format
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", formatted_datetime)



A word cloud is a visual representation of text data where the size of each word corresponds to its frequency or importance in the text. Here's how to interpret the size of the words in a word cloud:

Word Size:

Larger words: These words appear more frequently in the text or are considered more important based on the criteria used (e.g., frequency or relevance).
Smaller words: These words are less frequent or less important according to the criteria.
