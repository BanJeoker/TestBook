import nbformat as nbf
from nbconvert import HTMLExporter

# Load the notebook
with open('notebook.ipynb') as f:
    notebook = nbf.read(f, as_version=4)

# Filter out code cells, keeping only markdown and output cells
notebook.cells = [cell for cell in notebook.cells if cell.cell_type != 'code']

# Convert the modified notebook to HTML
html_exporter = HTMLExporter()
(body, resources) = html_exporter.from_notebook_node(notebook)

# Save the output to an HTML file
with open('output.html', 'w') as f:
    f.write(body)
