import nbformat as nbf
from nbconvert import HTMLExporter

# Load the notebook
with open('notebook.ipynb') as f:
    notebook = nbf.read(f, as_version=4)

# Filter out code cells but preserve their outputs
new_cells = []
for cell in notebook.cells:
    if cell.cell_type == 'code':
        if cell.outputs:
            # Create a new cell with the outputs only (no code box)
            new_cell = nbf.v4.new_code_cell()
            new_cell.cell_type = 'code'
            new_cell.outputs = cell.outputs
            new_cell.execution_count = None
            new_cells.append(new_cell)
    else:
        # Keep markdown and other cell types as they are
        new_cells.append(cell)

notebook.cells = new_cells

# Convert the modified notebook to HTML
html_exporter = HTMLExporter()
(body, resources) = html_exporter.from_notebook_node(notebook)

# Save the output to an HTML file
with open('output.html', 'w') as f:
    f.write(body)
