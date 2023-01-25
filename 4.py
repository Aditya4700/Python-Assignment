import random

def generate_random_data(num_items):
    data = []
    for i in range(num_items):
        data.append(random.randint(0, 100))
    return data

print(generate_random_data(10))