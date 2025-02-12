names = ['a', 'b']
num_repeat = 2  # Define the number of repeats

result = [f"{name}{i}" for name in names for i in range(1, num_repeat + 1)]
print(result)




import nbformat
import pandas as pd

# Load the notebook
with open("my_notebook.ipynb") as f:
    nb = nbformat.read(f, as_version=4)

# Extract cell contents
cells = [cell['source'] for cell in nb['cells'] if 'source' in cell]

# Convert to DataFrame
df = pd.DataFrame({'Notebook Content': cells})

# Save to Excel
df.to_excel("notebook_output.xlsx", index=False)
print("Notebook successfully saved as Excel")

