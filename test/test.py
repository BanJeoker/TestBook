

from rich.console import Console
from rich.markdown import Markdown
from rich.text impofrom rich.console import Console
from rich.markdown import Markdown
from rich.text import Text

console = Console()

# LLM output with markdown syntax
llm_output = """**Balance Sheet**
* Assets
* Liabilities
"""

# Render markdown
md = Markdown(llm_output)
text = console.render_str(str(md))  # Convert to raw string to find and re-style

# Now manually re-color the "**Balance Sheet**" text in red and bold
text_obj = Text.from_markup(str(md))
title = "Balance Sheet"
start = text_obj.plain.find(title)

if start != -1:
    end = start + len(title)
    text_obj.stylize("bold red", start, end)

console.print(text_obj)
rt Text

console = Console()

llm_output = "**Balance Sheet**, this is a summary of the company..."
# Detect and replace the bold title with colored rich markup
llm_output = llm_output.replace("**Balance Sheet**", "[bold red]Balance Sheet[/]")

console.print(llm_output, markup=True)


import asyncio

shared_counter = 0

async def increment():
    global shared_counter
    temp = shared_counter
    await asyncio.sleep(0.1)  # Simulate some delay
    shared_counter = temp + 1

async def main():
    await asyncio.gather(increment(), increment(), increment())

await main()
print("Final counter:", shared_counter)

