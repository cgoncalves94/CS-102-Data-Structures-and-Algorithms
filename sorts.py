import random

# Quick Sort algorithm
# Takes a list, start and end indices, and a comparison function as arguments
# Sorts the list based on the comparison function

def default_compare(x, y):
    return x > y

def quicksort(list, start, end, comparison_function=None):
    if comparison_function is None:
        comparison_function = default_compare
    if start >= end:
        return
    # Randomly select a pivot index.
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    list[end], list[pivot_idx] = list[pivot_idx], list[end]
    less_than_pointer = start
    for i in range(start, end):
        # Use the comparison function to compare pivot and list element.
        if comparison_function(pivot_element, list[i]):
            # Swap elements
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer += 1
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    quicksort(list, start, less_than_pointer - 1, comparison_function)
    quicksort(list, less_than_pointer + 1, end, comparison_function)
    return list