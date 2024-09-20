import nbformat as nbf
from nbconvert import HTMLExporter

# Load the notebook
with open('notebook.ipynb') as f:
    notebook = nbf.read(f, as_version=4)

# Create a new list for cells, ensuring that code cells retain only outputs
new_cells = []
for cell in notebook.cells:
    if cell.cell_type == 'code':
        # Check if the cell has outputs
        if cell.outputs:
            # Convert the outputs to new markdown cells
            for output in cell.outputs:
                if 'text' in output:
                    new_cells.append(nbf.v4.new_markdown_cell(output['text']))
                if 'data' in output and 'text/html' in output['data']:
                    new_cells.append(nbf.v4.new_markdown_cell(output['data']['text/html']))
    else:
        # Keep markdown cells and other types as they are
        new_cells.append(cell)

# Replace the notebook cells with the modified cells
notebook.cells = new_cells

# Convert the modified notebook to HTML
html_exporter = HTMLExporter()
(body, resources) = html_exporter.from_notebook_node(notebook)

# Save the output to an HTML file
with open('output.html', 'w') as f:
    f.write(body)
