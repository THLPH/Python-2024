def right_triangle(n):
    """
    Recursively print out a right triangle of *'s with n levels. Assume n > 0

    E.g. n = 4 -->  ****
                    ***
                    **
                    *
    """
    if n < 1:  # Base case: stop recursion when n is less than 1
        return
    else:
        print("*" * n)
        right_triangle(n - 1)

# Test case
right_triangle(4)  
# Expected output:
# ****
# ***
# **
# *
