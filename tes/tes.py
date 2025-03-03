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
