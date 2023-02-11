from random import randint

def generate_2d_array(row, col):
    numbers = [i for i in range(1, row*col+1)]
    random_2d_array = []
    for i in range(row):
        random_2d_array.append([numbers.pop(randint(0, len(numbers)-1)) for _ in range(col)])
    return random_2d_array