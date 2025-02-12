names = ['a', 'b']
num_repeat = 2  # Define the number of repeats

result = [f"{name}{i}" for name in names for i in range(1, num_repeat + 1)]
print(result)
