import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'cluster': ['0', '0', '0', '1', '1', '2', '2', '2', '0', '1'],
    'topic': ['A', 'B', 'A', 'A', 'C', 'B', 'B', 'C', 'C', 'A']
}
df = pd.DataFrame(data)

# Create a crosstab to count occurrences of each combination of cluster and topic
crosstab = pd.crosstab(df['cluster'], df['topic'])

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(crosstab, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap of Clusters vs. Topics')
plt.xlabel('Topic')
plt.ylabel('Cluster')
plt.show()


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

# Calculate the pairwise correlations
correlations = {
    ('Section1', 'Section2'): pivot_df['Section1'].corr(pivot_df['Section2']),
    ('Section1', 'Section3'): pivot_df['Section1'].corr(pivot_df['Section3']),
    ('Section2', 'Section3'): pivot_df['Section2'].corr(pivot_df['Section3'])
}

# Print the correlation values
for (section1, section2), correlation in correlations.items():
    print(f"Correlation between num_words in {section1} and {section2}: {correlation:.2f}")


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
