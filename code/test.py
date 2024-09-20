
{%- extends 'lab/index.html.j2' -%}

{% block input %}
<!-- This block will hide code cells -->
{%- endblock input %}


from IPython.display import display, HTML


# Your original text
text = "This is the revenue data. The revenue has increased this quarter."

# Replace 'revenue' with a highlighted version using HTML
highlighted_text = text.replace(
    'revenue',
    '<span style="background-color: yellow; font-weight: bold;">revenue</span>'
)

# Display the formatted HTML
html_output = f'<div style="white-space: nowrap;">{highlighted_text}</div>'

display(HTML(highlighted_text))


df = pd.DataFrame(data)

# Group by 'group' column and sum 'value1' and 'value2'
new_df = df.groupby('group', as_index=False).agg({'value1': 'sum', 'value2': 'sum'})

print(new_df)


import seaborn as sns
import matplotlib.pyplot as plt

# Assuming your DataFrame is named 'df' and the four columns are named:
# 'number_a', 'number_b', 'number_c', 'number_d'

# Set up a figure with two subplots, side by side (1 row, 2 columns)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Plot density for 'a' and 'b' in the first subplot
sns.kdeplot(df['number_a'], label='Number of A', fill=True, ax=axes[0])
sns.kdeplot(df['number_b'], label='Number of B', fill=True, ax=axes[0])
axes[0].axvline(df['number_a'].mean(), color='blue', linestyle='--', label='Mean A')
axes[0].axvline(df['number_b'].mean(), color='orange', linestyle='--', label='Mean B')
axes[0].set_title('Density Plot of A and B')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Density')
axes[0].legend()

# Plot density for 'c' and 'd' in the second subplot
sns.kdeplot(df['number_c'], label='Number of C', fill=True, ax=axes[1])
sns.kdeplot(df['number_d'], label='Number of D', fill=True, ax=axes[1])
axes[1].set_title('Density Plot of C and D')
axes[1].set_xlabel('Value')
axes[1].set_ylabel('Density')
axes[1].legend()

# Display the plot
plt.tight_layout()
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt

# Assuming your DataFrame is named 'df' and the four columns are named:
# 'number_a', 'number_b', 'number_c', 'number_d'

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot density for each metric
sns.kdeplot(df['number_a'], label='Number of A', fill=True)
sns.kdeplot(df['number_b'], label='Number of B', fill=True)
sns.kdeplot(df['number_c'], label='Number of C', fill=True)
sns.kdeplot(df['number_d'], label='Number of D', fill=True)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Density Plot of Document Metrics')

# Show the legend
plt.legend()

# Display the plot
plt.show()


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
