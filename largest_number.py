def largest_number(lst):
    """
    Finds the largest number in a list using recursion.

    Parameters:
        lst (list): A list of integers.

    Returns:
        int: The largest number in the list.

    Raises:
        ValueError: If the list is empty.
    """
    # Error handling: Check if the list is empty
    if not lst:
        raise ValueError("The list is empty!")

    # Base case: If the list has only one element, return it
    if len(lst) == 1:
        return lst[0]

    # Recursive case: Compare the first element with the largest of the rest of the list
    max_rest = largest_number(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest

# Test cases
try:
    print(largest_number([1, 4, 5, 3]))         # Output: 5
    print(largest_number([3, 1, 6, 8, 2, 4, 5])) # Output: 8
    print(largest_number([]))                  # This will raise an exception
except ValueError as e:
    print(e)
