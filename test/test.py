from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text

console = Console()

llm_output = """**Balance Sheet**
* Assets
* Liabilities
"""

# Step 1: Parse the Markdown into a Text object
md = Markdown(llm_output)
rendered = console.render_lines(md, pad=False)  # List of Text lines

# Step 2: Modify the title line (usually the first line)
title_line = rendered[0]
title_text = "Balance Sheet"

start = title_line.plain.find(title_text)
if start != -1:
    end = start + len(title_text)
    title_line.stylize("bold red", start, end)

# Step 3: Print each line manually
for line in rendered:
    console.print(line)
