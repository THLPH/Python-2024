def find_second_largest(numbers):
    """
    Given a list of numbers, return the second largest one in the list.

    We assume all numbers are positive and that len(numbers) >= 2
    """
    largest = float('-inf')  # Initialize to negative infinity
    second_largest = float('-inf')  # Initialize to negative infinity

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:  # Ensure no duplicates
            second_largest = num
    return second_largest

# Test case
print(find_second_largest([1, 3, 5, 6, 7, 8]))  # Expected output: 7
