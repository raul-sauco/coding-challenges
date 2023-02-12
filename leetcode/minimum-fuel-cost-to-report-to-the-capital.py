# 2477. Minimum Fuel Cost to Report to the Capital
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
#
# Tags: Tree - Depth-First Search - Breadth-First Search - Graph


import timeit
from math import ceil
from typing import List, Tuple


# We can use a postorder DFS, each node returns the number of people
# traveling and the amount of gas consumed to get everyone there, the
# parent looks at the number of people and computes the cost of getting
# everyone from the child to itself, then adds up all the costs plus
# the representative starting the journey there and returns that
# information to the parent.
#
# Time complexity: O(n) - We visit each node twice, once in the
# traversal and once when computing the results using the children's
# returns.
# Space complexity: O(n) - The call stack could grow to size n with a
# skewed tree.
#
# Runtime 1931 ms Beats 90.3%
# Memory 152.9 MB Beats 81.31%
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # Build an adjacency list.
        adj = [[] for _ in range(len(roads) + 1)]
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
        # A recursive depth-first search function that returns the
        # number of people traveling from that node upwards towards the
        # root, and the number of liters of fuel they have already used
        # to get there.
        def dfs(node: int, parent: int) -> Tuple[int]:
            fuel, passengers = 0, 1
            for child in adj[node]:
                if child == parent:
                    continue
                # The number of passengers that are traveling from the
                # child to this parent and the fuel that they used to
                # get to the child.
                f, p = dfs(child, node)
                # Compute the cost of traveling the edge between the
                # child and the parent. This equals 1 for each car
                # needed to bring everyone along.
                edge_cost = ceil(p / seats)
                # Add the costs to the overall costs to get here.
                fuel += f + edge_cost
                # Add the number of passengers to the ones already
                # traveling up-tree.
                passengers += p
            return (fuel, passengers)

        return dfs(0, -1)[0]


def test():
    executors = [Solution]
    tests = [
        [[], 1, 0],
        [[[0, 1], [0, 2], [0, 3]], 5, 3],
        [[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2, 7],
        [
            [
                [0, 1],
                [1, 2],
                [1, 3],
                [4, 2],
                [5, 3],
                [6, 3],
                [6, 7],
                [8, 6],
                [9, 0],
                [5, 10],
                [11, 9],
                [12, 5],
                [5, 13],
                [8, 14],
                [11, 15],
                [8, 16],
                [17, 0],
                [18, 7],
            ],
            13,
            19,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimumFuelCost(t[0], t[1])
                exp = t[2]
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
