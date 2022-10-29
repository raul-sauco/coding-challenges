# 743. Network Delay Time
# 🟠 Medium
#
# https://leetcode.com/problems/network-delay-time/
#
# Tags: Depth-First Search - Breath-First Search - Graph - Heap
# (Priority Queue) - Shortest Path

import timeit
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


# Use Dijkstra's algorithm to visit all the nodes saving the time it
# takes for the signal to arrive to any given node, return the maximum
# or -1 if the signal fails to reach all the nodes.
#
# Time complexity: O(e+n*log(n)) - Comes from Dijkstra's algorithm.
# Space complexity: O(e) - The adjacency list will contain all edges,
# the priority queue could as well.
#
# Runtime: 558 ms, faster than 82.49%
# Memory Usage: 16.1 MB, less than 69.91%
class Dijkstra:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Construct and adjacency list.
        neighbor_dict = defaultdict(list)
        for source, destination, time in times:
            neighbor_dict[source].append((destination, time))
        # Use a heap to pop the next node that the signal will arrive
        # to, heap elements are tuples of (edge value, node) and a
        # hash set to keep track of nodes we have visited.
        heap, seen = [(0, k)], {k}
        while heap:
            ttt, current = heappop(heap)
            seen.add(current)
            if len(seen) == n:
                return ttt
            # Add this node's neighbors to the priority queue.
            for neighbor, edge_weight in neighbor_dict[current]:
                if neighbor not in seen:
                    heappush(heap, (ttt + edge_weight, neighbor))

        return -1


def test():
    executors = [Dijkstra]
    tests = [
        [[[1, 2, 1]], 2, 1, 1],
        [[[1, 2, 1]], 2, 2, -1],
        [[[1, 2, 1], [2, 1, 3]], 2, 2, 3],
        [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.networkDelayTime(t[0], t[1], t[2])
                exp = t[3]
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
