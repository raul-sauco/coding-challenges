# 2013. Detect Squares
# 🟠 Medium
#
# https://leetcode.com/problems/detect-squares/
#
# Tags: Array - Hash Table - Design - Counting

import timeit
from collections import Counter, defaultdict
from typing import List


# Use a counter to store the count of each point that we add to the
# object. Use a dictionary to store a set of x coordinates that we see
# for each y coordinate.
#
# Time complexity add: O(1) - We add to a counter and a dictionary.
# Time complexity count: O(c) - Where c is the number of points at the
# same y axis than the input point. We will try to form one square with
# each point at the same axis y, and doing so takes O(1).
# Space complexity: O(n) - Where n is the number of points we add to the
# structure, for each point, we add one value to two dictionaries.
#
# Runtime: 642 ms, faster than 70.18%
# Memory Usage: 16 MB, less than 62.72%
class DetectSquares:
    def __init__(self):
        # Store the y values for all the points in a given x coordinate.
        self.dy = defaultdict(set)
        # A counter of all the points seen.
        self.points = Counter()

    # Add this point to the counter of points in the structure and add
    # its x coordinate to the set of x coordinates seen for this y
    # coordinate. O(1).
    def add(self, point):
        x, y = point
        self.dy[y].add(x)
        self.points[x, y] += 1

    # Return the count of squares that we could form using this point as
    # one of the vertex and any other three existing points as the
    # remaining vertexes of the square.
    def count(self, point):
        ax, ay = point
        count = 0
        # Iterate over the x coordinates of all points existing in this
        # y axis.
        for bx in self.dy[ay]:
            # Ignore points that are exactly the same as the given point.
            if bx == ax:
                continue
            b, side = (bx, ay), abs(ax - bx)
            # Using the given point a and the current b candidate, check
            # if their counterpart points c and d that could be used to
            # for a square of size "side" exist in the structure. Do
            # this search both upwards and downwards.
            for v in (side, -side):
                c, d = (ax, ay - v), (bx, ay - v)
                if c in self.points and d in self.points:
                    # If the points exist, compute the different number
                    # of ways in which we can form the square.
                    count += self.points[b] * self.points[c] * self.points[d]
        return count


# I misread the problem description and came up with an algorithm that
# detects rectangles, then modified it to detect only squares.
#
# Time complexity add: O(1) - We add to two dictionaries.
# Time complexity count: O(c^2) - Where c is the average number of
# points that share x and y axis. We will try to form one square with
# each point b at the same axis y and each point c at same axis x than b,
# and doing so takes O(1).
# Space complexity: O(n) - Where n is the number of points we add to the
# structure, for each point, we add one value to two dictionaries.
#
# Runtime: 347 ms, faster than 93.75%
# Memory Usage: 16 MB, less than 41.19%
class DetectRectangles:
    def __init__(self):
        # Dictionaries of points indexed by their horizontal values
        # and vertical values.
        self.dx = defaultdict(Counter)
        self.dy = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.dx[x][y] += 1
        self.dy[y][x] += 1

    def count(self, point: List[int]) -> int:
        ax, ay = point
        if ax not in self.dx or ay not in self.dy:
            return 0
        count = 0
        # Start with all the points on the same y axis as the given
        # point.
        for bx, b_count in self.dy[ay].items():
            # Ignore points that are exactly the same as the given point.
            if bx == ax:
                continue
            # Check all the points on the same x axis as the candidate.
            for cy, c_count in self.dx[bx].items():
                # Check either dictionary for point d
                if ax in self.dx and cy in self.dx[ax]:
                    d_count = self.dx[ax][cy]
                    # Need to modify the code to only add squares,
                    # remove the conditional check to detect rectangles.
                    if abs(ax - bx) == abs(ay - cy):
                        # The number of ways of building a rectangle
                        # multiplies with each point that we can choose.
                        count += b_count * c_count * d_count
        return count


def test():
    executors = [
        DetectSquares,
        DetectRectangles,
    ]
    tests = [
        [
            [
                "DetectSquares",
                "add",
                "add",
                "add",
                "count",
                "count",
                "add",
                "count",
                "add",
                "count",
                "add",
                "count",
            ],
            [
                [],
                [[3, 10]],
                [[11, 2]],
                [[3, 2]],
                [[11, 10]],
                [[14, 8]],
                [[11, 2]],
                [[11, 10]],
                [[3, 12]],
                [[11, 12]],
                [[11, 10]],
                [[11, 10]],
            ],
            [None, None, None, None, 1, 0, None, 2, None, 0, None, 2],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    argument = t[1][i][0]
                    result = getattr(sol, call)(argument)
                    exp = t[2][i]
                    assert result == exp, (
                        f"\033[93m» {result} <> {exp}\033[91m for"
                        + f" test {col}.{i} {call}({argument}) using "
                        + f"\033[1m{executor.__name__}"
                    )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
