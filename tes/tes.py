
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
