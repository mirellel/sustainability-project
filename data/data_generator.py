import random

def generate_data(file_path, num_values=1000, value_range=(1, 1000)):
    """
    Generates random integers and saves them to a file, one integer per line.
    
    Args:
        file_path (str): Path to the file where the data will be saved.
        num_values (int): Number of random integers to generate.
        value_range (tuple): Range (min, max) of random integers.
    """
    with open(file_path, 'w') as f:
        for _ in range(num_values):
            random_value = random.randint(value_range[0], value_range[1])
            f.write(f"{random_value}\n")

#Parameters
num_values = 10000 # Number of integers to generate
output_file = "/data/data_test_10k.txt" #CHANGE THIS TO PROPER PATH!
value_range = (1, 10000000)  # Range of values

generate_data(output_file, num_values=num_values, value_range=value_range)
