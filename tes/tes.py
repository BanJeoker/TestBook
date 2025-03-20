<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jupyter-style Print</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
</head>
<body>
    <div id="output"></div>
    <script>
        function jupyterPrint(text) {
            let outputDiv = document.getElementById("output");
            let newElement = document.createElement("p");
            newElement.innerHTML = marked.parse(text);
            outputDiv.appendChild(newElement);
        }

        jupyterPrint("Hello, **bold** world!");
        jupyterPrint("This is a _Markdown_ formatted string.");
    </script>
</body>
</html>
