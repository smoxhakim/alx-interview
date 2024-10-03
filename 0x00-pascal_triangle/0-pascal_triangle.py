#!/usr/bin/python3
def pascal_triangle(n):
    """Return an empty list for non-positive n"""

    if n <= 0:
        return []
    pas = [[1]]
    for r_number in range(1, n):
        r = [1]
        for j in range(1, r_number):
            element = pas[r_number - 1][j - 1] + pas[r_number - 1][j]
            r.append(element)
        r.append(1)
        pas.append(r)

    return pas