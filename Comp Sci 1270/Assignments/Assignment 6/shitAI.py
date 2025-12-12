import random

def generate_list_to_index_29():
    """
    Generates a list with indices from 0 to 29 (total of 30 elements),
    where each element has a random integer value between 1 and 5 (inclusive).
    """
    # The range function goes up to, but does not include, the end number.
    # We want 30 iterations (0 through 29).
    # The random.randint function is inclusive for both start and end numbers.
    random_list = [random.randint(1, 5) for _ in range(30)]
    return random_list

# Generate the list
my_list = generate_list_to_index_29()

# Print the list and its length for verification
print(f"Generated list of length {len(my_list)}:")
print(my_list)

# Optionally, print each index and value
print("\nIndex and Value pairs:")
for index, value in enumerate(my_list):
    print(f"Index {index}: {value}")