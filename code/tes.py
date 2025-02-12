import nbconvert

exporter = nbconvert.HTMLExporter()
body, resources = exporter.from_filename("your_notebook.ipynb")

with open("your_notebook.html", "w", encoding="utf-8") as f:
    f.write(body)
