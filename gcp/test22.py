text = """
This is a long line of text
that was broken unnecessarily.
"""
# Replace newlines with spaces
cleaned_text = ' '.join(line.strip() for line in text.splitlines())
print(cleaned_text)
