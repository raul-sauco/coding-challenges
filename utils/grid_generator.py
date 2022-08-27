# A helper function that generates grids with the given parameters.

import random
from typing import List


def generateGrid(m: int, n: int, a: int, b: int) -> List[List[int]]:
    grid = [[0] * m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            grid[row][col] = random.randint(a, b)
    return grid


# Example code to generate a grid of m*n size containing random integers
# with values between min_val and max_val.
cols = 5
rows = 4
min_val = -100
max_val = 100
print(generateGrid(cols, rows, min_val, max_val))
