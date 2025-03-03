import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'role': ['Manager', 'Analyst', 'Executive', 'Intern', 'Associate'],
    'salary': [80000, 60000, 120000, 30000, 50000]
})

# Define the custom sorting order
role_order = ['Intern', 'Analyst', 'Associate', 'Manager', 'Executive']

# Convert the column to a categorical type with the defined order
df['role'] = pd.Categorical(df['role'], categories=role_order, ordered=True)

# Sort by the defined order
df_sorted = df.sort_values('role')

# Display the sorted DataFrame
import ace_tools as tools
tools.display_dataframe_to_user(name="Sorted Roles", dataframe=df_sorted)


def is_numeric_string(value):
    if isinstance(value, str):  # Ensure input is a string
        try:
            float(value)  # Try converting to float
            return True
        except ValueError:
            return False
    return False  # If not a string, return False


import pandas as pd

pd.set_option('display.float_format', '{:.10f}'.format)  # Show full numbers with 10 decimal places


import pandas as pd

# Sample DataFrame
data = {'ID': [1, 1, 1, 2, 2, 3, 3, 3],
        'Category': ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'],
        'Text': ['apple', 'banana', 'cherry', 'dog', 'elephant', 'fish', 'goat', 'hen']}
df = pd.DataFrame(data)

# Group by 'ID' and 'Category', and concatenate 'Text' column
grouped_df = df.groupby(['ID', 'Category'])['Text'].agg('.'.join).reset_index()

# Add as a new column (optional, if you want to modify the original DataFrame)
grouped_df['Aggregated_Text'] = grouped_df['Text']

# Drop the old 'Text' column if not needed
grouped_df = grouped_df.drop(columns=['Text'])

# Display new DataFrame
print(grouped_df)



import pandas as pd
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

# Sample DataFrame
data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [95, 87, 78]
}
df = pd.DataFrame(data)

# Function to create XML from DataFrame
def df_to_xml(df):
    root = ET.Element("Records")  # Root Element

    for _, row in df.iterrows():
        record = ET.SubElement(root, "Record")  # Each row is a Record

        for col in df.columns:
            field = ET.SubElement(record, col)
            field.text = str(row[col])  # Convert values to string

    return root

# Function to pretty-print XML
def pretty_print_xml(root):
    xml_str = ET.tostring(root, encoding="utf-8")  # Convert XML tree to string
    parsed = minidom.parseString(xml_str)  # Parse string into DOM
    return parsed.toprettyxml(indent="  ")  # Pretty-print XML with indentation

# Generate XML and Pretty Print
xml_root = df_to_xml(df)
pretty_xml = pretty_print_xml(xml_root)

print(pretty_xml)







import pandas as pd
import xml.etree.ElementTree as ET

# Sample DataFrame

data = {
    "ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [95, 87, 78]
}
df = pd.DataFrame(data)

# Function to create XML from DataFrame
def df_to_xml(df):
    root = ET.Element("Records")  # Root Element

    for _, row in df.iterrows():
        record = ET.SubElement(root, "Record")  # Each row is a Record

        for col in df.columns:
            field = ET.SubElement(record, col)
            field.text = str(row[col])  # Convert values to string

    return ET.tostring(root, encoding="utf-8").decode("utf-8")

# Generate XML String
xml_string = df_to_xml(df)

# Print XML
print(xml_string)
