# Minimum Area Rectangle
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/minimum-area-rectangle
#
# Tags: Array - Geometry

import timeit
from collections import defaultdict
from typing import List


# Create two hashmaps of all points indexed by their x coordinates in
# one and by their y coordinates in the other one. We get a sorted list
# of all x coordinates that contain any points, and start iterating over
# them from left to right, for each coordinate, we get a sorted list of
# all the y points at that x coordinate and start iterating over any
# possible combination of two with y1 being the lower one and y2 being
# the higher one, for any y2 value, we iterate over all x values in that
# axis, now we have all the coordinates that we need to construct a
# rectangle and we just need to check if the last point exists in O(1).
#
# Time complexity: O(n*m) - Where m is the maximum number of points in
# a given axis. Worst case all the points are in the same axis and we
# end up iterating over every single pair in O(n^2), average case is
# probably something like O(n*log(n)) where the points are evenly
# distributed and we don't have many points in the same axis, best case
# would be O(n) and it would be when each x and y axis contain a maximum
# of 2 points, in that case we would only visit each point once.
# Space complexity: O(n) - Both hashmaps have as many entries as points
# there are in the input array.
class Solution:
    def minimumAreaRectangle(self, points: List[int]) -> int:
        # Create hashmaps of points indexed by their x and y coordinates.
        xs, ys = defaultdict(set), defaultdict(set)
        for x, y in points:
            xs[x].add(y)
            ys[y].add(x)
        # Create a sorted list of the x values in which we can find
        # any points.
        x_values = sorted(xs.keys())
        # The smallest rectangle found.
        res = float("inf")
        # Iterate from the bottom-left corner trying to build rectangles.
        for x1 in x_values:
            y_values = sorted(xs[x1])
            for i in range(len(y_values)):
                y1 = y_values[i]
                for j in range(i + 1, len(y_values)):
                    y2 = y_values[j]
                    for x2 in ys[y2]:
                        if x2 <= x1:
                            continue
                        if x2 in ys[y1]:
                            res = min(res, (y2 - y1) * (x2 - x1))
        return 0 if res == float("inf") else res


def test():
    executors = [Solution]
    tests = [
        [[[0, 0], [4, 4], [8, 8], [0, 8]], 0],
        [[[0, 0], [4, 4], [8, 8], [0, 8], [0, 4], [6, 0], [6, 4]], 24],
        [[[-4, 4], [4, 4], [4, -2], [-4, -2], [0, -2], [4, 2], [0, 2]], 16],
        [
            [
                [1, 5],
                [5, 1],
                [4, 2],
                [2, 4],
                [2, 2],
                [1, 2],
                [4, 5],
                [2, 5],
                [-1, -2],
            ],
            3,
        ],
        [
            [
                [-4, 4],
                [4, 4],
                [4, -2],
                [-4, -2],
                [0, -2],
                [4, 2],
                [0, 2],
                [0, 4],
                [2, 3],
                [0, 3],
                [2, 4],
            ],
            2,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimumAreaRectangle(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
