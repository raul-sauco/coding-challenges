# 149. Max Points on a Line
# 🔴 Hard
#
# https://leetcode.com/problems/max-points-on-a-line/
#
# Tags: Array - Hash Table - Math - Geometry

import timeit
from collections import defaultdict
from typing import List, Tuple


# Create a dictionary with lines as the keys and all the points that
# belong to a line as the values. To define a line, we use its slope and
# y-intercept values, this uniquely identifies all lines formed by any
# two points in the input. Once we have assigned each point to all the
# lines where it belongs, we check which line has the most points.
#
# Time complexity: O(n^2) - For each pair of points a, b, we compute its
# slope and y-intercept values to use as keys and add them to the lines
# dictionary.
# Space complexity: O(n^2) - The lines dictionary could potentially
# have an entry for each combination of two points in the input.
#
# Runtime 150 ms Beats 63.60%
# Memory 38.3 MB Beats 8.91%
class GroupByLines:
    # Get the dictionary key of the line between two given points.
    def getLineKey(self, ax: int, ay: int, bx: int, by: int) -> Tuple[float]:
        m = (by - ay) / (bx - ax) if bx != ax else float("inf")
        c = (ay - m * ax) if m != float("inf") else ax
        # Returns a tuple of (slope, constant) that uniquely defines a
        # line in a plane.
        return (m, c)

    def maxPoints(self, points: List[List[int]]) -> int:
        res, lines = 1, defaultdict(set)
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                # Compute the lines between all points and add them to
                # the dictionary. O(n^2)
                a, b = points[i], points[j]
                key = self.getLineKey(a[0], a[1], b[0], b[1])
                lines[key].add((a[0], a[1]))
                lines[key].add((b[0], b[1]))
        for points_in_line in lines.values():
            res = max(res, len(points_in_line))
        return res


# Improve the previous solution only storing the number of points per
# slope per each point, instead of all the points combinations. This
# solution has the same time complexity in theory, but it performs much
# better because it only needs to perform an addition, instead of
# hashing a tuple, when we add an element to the count. The memory
# complexity is obviously much better because we only store n entries
# in the dictionary, recreating it for each point a and only storing the
# slopes that it forms with all other points b, O(n) instead of all the
# combinations of a and b, like the previous solution in O(n^2).
#
# Time complexity: O(n^2) - For each pair of points a, b, we compute its
# slope and y-intercept values to use as keys and add them to the lines
# dictionary.
# Space complexity: O(n) - The lines dictionary could potentially
# have an entry for each point in the input.
#
# Runtime 53 ms Beats 99.88%
# Memory 13.9 MB Beats 94.26%
class PerPoint:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points) - 1):
            lines = {}
            ax, ay = points[i]
            for j in range(i + 1, len(points)):
                # Compute the line slope.
                bx, by = points[j]
                # Get the key inline to avoid function call.
                key = (by - ay) / (bx - ax) if ax != bx else float("inf")
                if key not in lines:
                    lines[key] = 2
                else:
                    lines[key] += 1
                # res = max(res, lines[key])
                if lines[key] > res:
                    res = lines[key]
        return res


def test():
    executors = [
        GroupByLines,
        PerPoint,
    ]
    tests = [
        [[[1,1],[2,2],[3,3]], 3],
        [[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4],
        [[[7,3],[19,19],[-16,3],[13,17],[-18,1],[-18,-17],[13,-3],[3,7],[-11,12],[7,19],[19,-12],[20,-18],[-16,-15],[-10,-15],[-16,-18],[-14,-1],[18,10],[-13,8],[7,-5],[-4,-9],[-11,2],[-9,-9],[-5,-16],[10,14],[-3,4],[1,-20],[2,16],[0,14],[-14,5],[15,-11],[3,11],[11,-10],[-1,-7],[16,7],[1,-11],[-8,-3],[1,-6],[19,7],[3,6],[-1,-2],[7,-3],[-6,-8],[7,1],[-15,12],[-17,9],[19,-9],[1,0],[9,-10],[6,20],[-12,-4],[-16,-17],[14,3],[0,-1],[-18,9],[-15,15],[-3,-15],[-5,20],[15,-14],[9,-17],[10,-14],[-7,-11],[14,9],[1,-1],[15,12],[-5,-1],[-17,-5],[15,-2],[-12,11],[19,-18],[8,7],[-5,-3],[-17,-1],[-18,13],[15,-3],[4,18],[-14,-15],[15,8],[-18,-12],[-15,19],[-9,16],[-9,14],[-12,-14],[-2,-20],[-3,-13],[10,-7],[-2,-10],[9,10],[-1,7],[-17,-6],[-15,20],[5,-17],[6,-6],[-11,-8]], 6],  # fmt: skip
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.maxPoints(t[0])
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
