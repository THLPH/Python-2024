def three_sum(numbers, n):
    """
    Given a list of numbers and a target n, return True if any three of the numbers add up to n and False otherwise.
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):  # Start from i+1 to avoid duplicates
            for k in range(j + 1, len(numbers)):  # Start from j+1 to avoid duplicates
                if numbers[i] + numbers[j] + numbers[k] == n:
                    return True
    return False

# Test cases
print(three_sum([5, 6, 7, 8, 9], 4))  # Expected output: False
print(three_sum([5, 6, 7, 8, 9], 21))  # Expected output: True
print(three_sum([5, 6, 7, 8, 9], 15))  # Expected output: False
