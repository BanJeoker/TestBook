import importlib.util

# Path to the .py file
file_path = '/Users/yourname/projects/myscript.py'

# Module name can be anything
module_name = 'myscript'

# Load the module
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Now you can use functions from that module
result = module.my_function()
