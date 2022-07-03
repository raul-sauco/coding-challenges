# https://leetcode.com/problems/erect-the-fence/

# https://en.wikipedia.org/wiki/Convex_hull_algorithms

import timeit
from math import atan2
from random import randint
from typing import List

from graham_scan import scatterPlot


# Runtime: 652 ms, faster than 9.20% of Python3 online submissions for Erect the Fence.
# Memory Usage: 15 MB, less than 17.24 % of Python3 online submissions for Erect the Fence.
class GrahamScan:

    # https://en.wikipedia.org/wiki/Polar_coordinate_system
    # Calculate the angle between the x axis and the vector between two given points
    def polarAngle(self, p0: List[int], p1: List[int]) -> float:
        return atan2(p1[1]-p0[1], p1[0]-p0[0])

    # Sort the points by teh polar angle of the vector between the anchor and
    # the given point. Smaller first. Points with the same angle from the
    # anchor will be ordered by distance with the closest first.

    def sort(self, points: List[List[int]], anchor: List[int]) -> List[List[int]]:

        # Calculate the square of the scalar distance between two given points
        def distance(p) -> float:
            # Avoid calculating the square root to improve performance
            return (p[1]-anchor[1])**2 + (p[0]-anchor[0])**2

        if len(points) <= 1:
            return points
        s, e, l = [], [], []
        pivot_angle = self.polarAngle(
            anchor, points[randint(0, len(points) - 1)])
        for pt in points:
            # Do not add the anchor to the sorted points
            if pt == anchor:
                continue
            angle = self.polarAngle(anchor, pt)
            if angle < pivot_angle:
                s.append(pt)
            elif angle == pivot_angle:
                e.append(pt)
            else:
                l.append(pt)
        return self.sort(s, anchor) + sorted(e, key=distance) + self.sort(l, anchor)

    # The original Graham Scan algorithm only takes vertices into account,
    # but the problem asks us to return all points "in the fence"
    # We need to keep points in a straight line, for the algorithm to work,
    # points leaving the anchor need to be ordered from closer to more distant
    # but points going back to the anchor need to be ordered from further away
    # to closer, reverse the sorting order of all points with the greatest
    # angle from the anchor.
    def reverseTail(self, points: List[List[int]], anchor: List[int]) -> List[List[int]]:
        # Make sure that the point set is not a straight line, no point reversing the points then
        if self.polarAngle(anchor, points[0]) != self.polarAngle(anchor, points[-1]):
            tail = [points.pop()]
            while self.polarAngle(anchor, points[-1]) == self.polarAngle(anchor, tail[0]):
                tail.append(points.pop())
            points.extend(tail)
            return points
        return points

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) < 4:
            return trees

        def det(p1, p2, p3):
            return (p2[0]-p1[0]) * (p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

        # List to store the perimeter trees
        p = []
        anchor = min(trees, key=lambda x: (x[1], x[0]))

        p.append(anchor)
        trees = self.sort(trees, anchor)
        trees = self.reverseTail(trees, anchor)
        # The anchor was removed on the sorting step. Otherwise remove here
        # del trees[trees.index(anchor)]
        # Add the furthest clockwise point to the hull
        p.append(trees[0])
        for t in trees[1:]:
            while det(p[-2], p[-1], t) < 0:
                del p[-1]
                if len(p) < 2:
                    break
            p.append(t)
        return p


class Monotone:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        points = sorted(map(tuple, points), key=lambda x: (x[0], x[1]))

        def sign(o, a, b):
            return (a[0]-o[0]) * (b[1]-o[1]) - (b[0]-o[0]) * (a[1]-o[1])

        def build(points):
            hull = []
            for p in points:
                while len(hull) >= 2 and sign(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull += p,
            return hull

        return list(set(build(points) + build(points[::-1])))

def test():
    executors = [
        {'executor': GrahamScan, 'title': 'GrahamScan', },
        # {'executor': Monotone, 'title': 'Monotone', },
    ]
    tests = [
        [
            [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 1], [
                3, 0], [2, 0], [1, 0], [1, 1], [4, 3], [3, 3], [4, 2]],
            [[0, 0], [4, 2], [1, 0], [0, 2], [3, 0],
                [2, 0], [4, 3], [3, 3], [0, 1]],
        ],
        [[[3, 0]], [[3, 0]]],
        [[[0, 8], [9, 8], [2, 4]], [[0, 8], [9, 8], [2, 4]]],
        [[[3, 0], [4, 1], [5, 0]], [[3, 0], [4, 1], [5, 0]]],
        [[[3, 0], [4, 0], [5, 0]], [[3, 0], [4, 0], [5, 0]]],
        [
            [[3, 0], [4, 0], [5, 0], [6, 1], [7, 2], [7, 3], [7, 4], [6, 5], [5, 5], [
                4, 5], [3, 5], [2, 5], [1, 4], [1, 3], [1, 2], [2, 1], [4, 2], [0, 3]],
            [[4, 5], [2, 5], [6, 1], [3, 5], [2, 1], [1, 4], [1, 2], [7, 4], [
                7, 3], [7, 2], [3, 0], [0, 3], [5, 0], [5, 5], [4, 0], [6, 5]],
        ],
        [[[3, 2], [1, 2], [3, 4], [2, 2]], [[3, 2], [1, 2], [3, 4], [2, 2]]],
        [
            [[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2], ],
            [[1, 1], [2, 0], [3, 3], [2, 4], [4, 2], ],
        ],
        [[], []],
        [[[1, 2], [2, 2], [4, 2]], [[4, 2], [2, 2], [1, 2]]],
        [
            [
                [25, 5], [24, 18], [31, 43], [35, 50], [24, 22], [47, 25],
                [1, 28], [37, 28], [15, 40], [30, 36], [3, 31], [19, 29],
                [44, 36], [38, 39], [7, 32], [14, 4], [32, 20], [13, 43],
                [37, 46], [31, 2], [42, 31], [1, 48], [17, 49], [6, 23],
                [36, 49], [13, 4], [26, 23], [21, 26], [1, 49], [9, 34],
                [10, 31], [35, 12], [49, 21], [17, 3], [30, 3], [3, 42],
                [43, 23], [6, 10], [35, 21], [37, 34], [47, 38], [27, 21],
                [33, 1], [39, 45], [16, 2], [3, 35], [29, 3], [3, 41],
                [32, 8], [18, 22], [18, 37], [41, 21], [24, 41], [27, 6],
                [24, 43], [41, 39], [33, 12], [9, 9], [25, 1], [40, 1],
                [1, 17], [24, 13], [10, 40], [14, 43], [10, 45], [7, 42],
                [18, 3], [20, 40], [0, 49], [13, 27], [44, 17], [36, 2],
                [11, 49], [18, 18], [22, 43], [0, 3], [2, 3], [50, 41],
                [4, 38], [27, 24], [16, 36], [19, 3], [25, 30], [10, 20],
                [2, 32], [48, 18], [33, 36], [17, 0], [0, 47], [29, 7],
                [27, 20], [38, 27], [4, 1], [44, 14], [32, 17], [44, 50],
                [48, 16], [44, 13], [28, 20], [7, 25],
            ],
            [
                [17, 0], [40, 1], [48, 16], [49, 21], [50, 41], [44, 50],
                [35, 50], [0, 49], [0, 47], [0, 3], [4, 1],
            ],
        ],
        [
            [
                [7, 21], [28, 6], [23, 33], [17, 36], [28, 9], [2, 27],
                [2, 12], [45, 34], [3, 18], [47, 14], [13, 35], [34, 48],
                [27, 24], [41, 46], [26, 4],
            ],
            [
                [26, 4], [47, 14], [45, 34], [41, 46], [34, 48], [13, 35],
                [2, 27], [2, 12],
            ],
        ],
        [[[1, 5]], [[1, 5]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for i, t in enumerate(tests):
                sol = executor['executor']()
                result = sol.outerTrees(t[0])
                expected = t[1]
                assert len(result) == len(
                    expected), f'length {len(result)} != {len(expected)} on test {i}'
                for r in result:
                    assert r in expected, f'Result {r} is not expected on test {i}'
                for e in expected:
                    assert e in result, f'Expected {e} not found on test {i}'
                # assert result == expected, f'{result} != {expected} for {t[0]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(
            executor['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()


def plot():
    sol = GrahamScan()
    input = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 1], [
        3, 0], [2, 0], [1, 0], [1, 1], [4, 3], [3, 3], [4, 2]]
    fence = sol.outerTrees(input)
    scatterPlot(input, fence)


# plot()
