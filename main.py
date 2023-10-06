import numpy as np
import matplotlib.pyplot as plt
import random

randomList = random.sample(range(100), 100)
y = random.sample(range(100), 100)
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

plt.plot(randomList, y)
plt.show