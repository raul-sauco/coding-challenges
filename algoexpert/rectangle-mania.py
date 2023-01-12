# Rectangle Mania
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/rectangle-mania
#
# Tags: Graph - Math - Geometry

import timeit
from collections import defaultdict
from typing import List


# One intuitive solution tries to find rectangles choosing one of its
# corners as the starting one and then traveling clock, or counter, wise
# over all the other vertices. The vertices are easy to find because
# we know that they are in the same axis as their neighbors. To make
# sure that we do double count rectangles, we can use a set that
# contains a sorted tuple of 4 tuples.
#
# Time complexity: O(n^2) - For each coordinate, we visit all other
# coordinates, once we have two, we can find the other two coordinates
# faster.
# Space complexity: O(n) - The dictionaries will contain all points in
# the input.
class Clockwise:
    def rectangleMania(self, coords) -> int:
        # A set of all points to find the fourth coordinate in O(1).
        points = set(map(tuple, coords))
        squares = set()
        # Dictionaries of points keyed by their x and y points.
        xs, ys = defaultdict(list), defaultdict(list)
        for x, y in coords:
            xs[x].append((x, y))
            ys[y].append((x, y))
        # Iterate over every combination of two points in this x-axis
        # value using them to try to form squares.
        for x_coords in xs.values():
            for i in range(len(x_coords)):
                ax, ay = x_coords[i]
                for j in range(i + 1, len(x_coords)):
                    bx, by = x_coords[j]
                    if ax != bx:
                        raise Exception(
                            "WTF, x coordinates are supposed to be the same"
                        )
                    # Iterate over all the points with the same y
                    # coordinate as b.
                    for cx, cy in ys[by]:
                        # Skip points along the same x-axis.
                        if cx == ax:
                            continue
                        # If the fourth point of the square exists,
                        # add it to the result.
                        if (cx, ay) in points:
                            squares.add(
                                tuple(
                                    sorted(
                                        (
                                            (ax, ay),
                                            (bx, by),
                                            (cx, cy),
                                            (cx, ay),
                                        )
                                    )
                                )
                            )
        return len(squares)


# We can make the code more readable using the observation that, if we
# find two points situated in different x and y axis, they could form
# two opposite corners of the rectangle, then we could check if their
# matching corners exist in O(1). If we sort the points and iterate over
# them using two nested loops, we can consider the first point the
# bottom left and check if the second could be the top/right, which
# means that both its x and y value need to be greater than, if it can,
# then we check if the two matching corners exist. This algorithm
# prevents duplicates because we only iterate over each combination of
# bottom/left and top/right points once.
#
# Time complexity: O(n^2) - We iterate over all combinations of two
# points in the input.
# Space complexity: O(n) - The hash set contains all the points in the
# input. We use it to find the third and fourth points in O(1). If we
# could not use extra space, we could find these points in O(log(n)) in
# the sorted array, giving an overall time complexity of O(log(n)*n^2).
class TwoCorners:
    def rectangleMania(self, coords: List[List[int]]) -> int:
        # Sort the points by x, then y coordinates.
        coords.sort()
        # Create a set of existing points to check in O(1).
        points = set(map(tuple, coords))
        res = 0
        # Get the bottom/left point.
        for i in range(len(coords)):
            # Check if this point could be the top/right point of a
            # rectangle.
            ax, ay = coords[i]
            for j in range(i + 1, len(coords)):
                # Skip points in the same x or y axis as a.
                cx, cy = coords[j]
                # Only interested in points higher up and to the right.
                if ax >= cx or ay >= cy:
                    continue
                if (ax, cy) in points and (cx, ay) in points:
                    res += 1
        return res


def test():
    executors = [
        Clockwise,
        TwoCorners,
    ]
    tests = [
        [[[1, 1], [1, 3], [2, 1], [2, 0], [3, 1], [3, 2]], 0],
        [[[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]], 6],
        [
            [
                [0, 0],
                [0, 1],
                [1, 1],
                [1, 0],
                [2, 1],
                [2, 0],
                [3, 1],
                [3, 0],
                [1, 3],
                [3, 3],
                [0, -4],
                [3, -4],
            ],
            10,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.rectangleMania(t[0])
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
