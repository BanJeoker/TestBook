from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text

console = Console()

llm_output = "**Balance Sheet**, this is a summary of the company..."
# Detect and replace the bold title with colored rich markup
llm_output = llm_output.replace("**Balance Sheet**", "[bold red]Balance Sheet[/]")

console.print(llm_output, markup=True)
