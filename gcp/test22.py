import re

# Financial text example
financial_text = """
* revenue: revenue increased a to b. because of strong demand in Q3.\n
* profit: profit increased a to b. due to cost-saving measures.\n
* expenses: expenses decreased a to b. owing to lower raw material prices.\n
"""

# List of metrics to search for
metrics = ["revenue", "profit", "expenses"]

# List to store the elevator analysis
elevator_analysis = []

# Regular expression pattern to capture the first sentence for each metric
for metric in metrics:
    pattern = rf"\* {metric}: (.*?\.?)"  # Match "* metric:" followed by the first sentence
    match = re.search(pattern, financial_text, re.IGNORECASE)  # Case-insensitive search
    if match:
        elevator_analysis.append(match.group(1))  # Append the captured sentence

# Output the result
print(elevator_analysis)


from concurrent.futures import ThreadPoolExecutor, as_completed

def task(n):
    return n * n

with ThreadPoolExecutor() as executor:
    # Submit tasks
    futures = [executor.submit(task, i) for i in range(5)]

    # Process futures as they complete
    for future in as_completed(futures):
        try:
            result = future.result()  # Retrieve result
            print(f"Task completed with result: {result}")
        except Exception as e:
            print(f"Task raised an exception: {e}")

