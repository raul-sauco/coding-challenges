# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# 🟠 Medium
#
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
#
# Tags: Depth-First Search - Breadth-First Search - Graph

import timeit
from typing import List


# Since we have n-1 roads and we are guaranteed that we will be able to
# reach the root from all nodes after reversing some, or none, roads,
# that means that there is one road between any two nodes. We can use
# two structures, a set of nodes that we have visited, and a stack, or
# queue, or nodes that are able to get to the root node, as well as a
# counter of the number of connections that we need to reverse. We start
# by visiting 0 and checking all the roads that are connected to it, any
# road that leads away from 0, will need to be reversed, we do it, and
# add the node at the end of that road to the stack to be processed
# because that node now can access the root node, when the road leads to
# the node that we are visiting, we add the source node to the stack to
# be processed.
#
# Time complexity: O(n) - Even though we have nested loops, the inner
# loop will run only a total of 2*(n-1) times, which is the number of
# connections that we have in our "roads" structure .
# Space complexity: O(n) - The roads structure will have 2*(n-1)
# elements, the stack could grow to size n and the set will grow to size
# n because we will visit all nodes.
#
# Runtime 1132 ms Beats 98.48%
# Memory 41.5 MB Beats 93.33%
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = [[] for _ in range(n)]
        for a, b in connections:
            roads[a].append((a, b))
            roads[b].append((a, b))
        need_reversing = 0
        stack = [0]
        seen = set([0])
        while stack:
            current = stack.pop()
            for a, b in roads[current]:
                # If the road is from current to another node, it needs
                # to be reversed.
                if a == current:
                    if b not in seen:
                        seen.add(b)
                        need_reversing += 1
                        stack.append(b)
                # If the road goes from b to a, b can reach the root.
                elif a not in seen:
                    seen.add(a)
                    stack.append(a)
        return need_reversing


def test():
    executors = [Solution]
    tests = [
        [3, [[1, 0], [2, 0]], 0],
        [5, [[1, 0], [1, 2], [3, 2], [3, 4]], 2],
        [6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minReorder(t[0], t[1])
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
