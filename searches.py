# Binary Search for list of dictionaries
def binary_search(array, target, key):
    """Perform a binary search on a sorted list of dictionaries."""

    low = 0  # Initialize the low pointer
    high = len(array) - 1  # Initialize the high pointer
    
    # Continue until low pointer is less than or equal to the high pointer
    while low <= high:
        mid = (low + high) // 2  # Compute the mid-point index

        # If the target is found, return its index
        if array[mid][key] == target:
            return mid
        # If the mid-point value is less than the target,
        # move the low pointer to the right of mid-point
        elif array[mid][key] < target:
            low = mid + 1
        # If the mid-point value is greater than the target,
        # move the high pointer to the left of mid-point
        else:
            high = mid - 1
            
    return -1  # Return -1 if the target is not found
