import random



def is_sorted(restaurant_list, key):
    """Check if the restaurant list is sorted by the given key."""
    return all(restaurant_list[i][key] <= restaurant_list[i + 1][key] for i in range(len(restaurant_list) - 1))

def compare_by_key(key):
    """Returns a custom comparison function that compares dictionary elements based on the specified key"""
    
    def compare(x, y):
        return x[key] > y[key]
    return compare

def default_compare(x, y):
    """Compares two elements and returns True if x is greater than y."""
    return x > y

def quicksort(list, start, end, comparison_function=None):
    """ Takes a list, start and end indices, and a comparison function as arguments
        Sorts the list based on the comparison function """
        
    # If no custom comparison function is provided, use the default one
    if comparison_function is None:
        comparison_function = default_compare
        
    # Base case: return if the start index is greater or equal to the end index
    if start >= end:
        return

    # Randomly select a pivot index to improve performance on sorted arrays
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = list[pivot_idx]
    
    # Move the pivot element to the end of the array
    list[end], list[pivot_idx] = list[pivot_idx], list[end]
    
    # Pointer for elements less than the pivot
    less_than_pointer = start
    
    # Iterate through the array and move elements smaller than the pivot to the left
    for i in range(start, end):
        # Use the comparison function to compare pivot and list element.
        if comparison_function(pivot_element, list[i]):
            # Swap elements
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer += 1

    # Move the pivot element to its final position
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    
    # Recursively sort the two sub-arrays
    quicksort(list, start, less_than_pointer - 1, comparison_function)
    quicksort(list, less_than_pointer + 1, end, comparison_function)
    return list