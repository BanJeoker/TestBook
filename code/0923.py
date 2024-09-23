import pandas as pd
import string
import seaborn as sns
import matplotlib.pyplot as plt

# Sample word lists
list1 = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
list2 = ['apricot', 'blueberry', 'cantaloupe', 'dragonfruit', 'eggplant', 'fig', 'guava']

# Initialize a dictionary to hold the data
data = {'list1': [], 'list2': []}
index = list(string.ascii_lowercase)  # ['a', 'b', ..., 'z']

# Function to get words starting with a specific letter
def get_words_starting_with(words, letter):
    return [word for word in words if word.lower().startswith(letter)]

# Populate the data dictionary
for letter in index:
    words1 = get_words_starting_with(list1, letter)
    words2 = get_words_starting_with(list2, letter)
    data['list1'].append(', '.join(words1) if words1 else '')
    data['list2'].append(', '.join(words2) if words2 else '')

# Create the DataFrame
df = pd.DataFrame(data, index=index)
df.index.name = 'Starting Letter'

# Display the DataFrame
print(df)

# Create a binary dataframe for visualization
binary_data = {
    'list1': [1 if word else 0 for word in data['list1']],
    'list2': [1 if word else 0 for word in data['list2']]
}
binary_df = pd.DataFrame(binary_data, index=index)
binary_df.index.name = 'Starting Letter'

# Plot the heatmap
plt.figure(figsize=(8, 12))
sns.heatmap(binary_df, annot=True, cmap='YlGnBu', cbar=False, linewidths=.5)
plt.title('Presence of Words Starting with Each Letter in List1 and List2')
plt.show()

# Save the DataFrame
df.to_csv('word_comparison.csv')
