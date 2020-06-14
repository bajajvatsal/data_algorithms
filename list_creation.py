import random


def unordered_array(n):
    array = [i for i in range(1, n + 1)]
    random.shuffle(array)
    return array
