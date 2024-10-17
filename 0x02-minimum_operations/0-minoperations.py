#!/usr/bin/python3
#!/usr/bin/python3

"""
Minimum Operations
"""


def minOperations(n):
    """
    Minimum Operations
    """

    i = 1
    y = 0
    count = 0
    while i < n:
        remainder = n - i
        if (remainder % i == 0):
            y = i
            i += y
            count += 2
        else:
            i += y
            count += 1
    return count