import nbconvert

exporter = nbconvert.HTMLExporter()
body, resources = exporter.from_filename("your_notebook.ipynb")

with open("your_notebook.html", "w", encoding="utf-8") as f:
    f.write(body)



import nbformat
from nbconvert import HTMLExporter

# Load the notebook
with open("your_notebook.ipynb") as f:
    notebook = nbformat.read(f, as_version=4)

# Remove input cells
for cell in notebook.cells:
    if cell.cell_type == "code":
        cell.source = ""  # Remove code content

# Convert to HTML
exporter = HTMLExporter()
body, resources = exporter.from_notebook_node(notebook)

# Save the HTML output
with open("your_notebook.html", "w", encoding="utf-8") as f:
    f.write(body)

