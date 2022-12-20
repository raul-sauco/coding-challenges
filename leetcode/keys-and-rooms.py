# 841. Keys and Rooms
# 🟠 Medium
#
# https://leetcode.com/problems/keys-and-rooms/
#
# Tags: Depth-First Search - Breadth-First Search - Graph

import timeit
from typing import List

# Use a stack, a queue would work as well, to store rooms for which we
# have gotten the keys but have not visited yet, visit them by popping
# them from the stack and, for each key found for a room we have not
# visited yet, add it to the stack and mark the room as visited.
#
# Time complexity: O(n) - We will visit all rooms once at most.
# Space complexity: O(n) - The visited array and the stack will grow in
# size linearly with the size of the input.
#
# Runtime 70 ms Beats 89.18%
# Memory 14.4 MB Beats 57.55%
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Use an array instead of a set to save hashing work.
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]
        while stack:
            for key in rooms[stack.pop()]:
                if not visited[key]:
                    stack.append(key)
                    visited[key] = True
        return all(visited)


def test():
    executors = [Solution]
    tests = [
        [[[1], [2], [3], []], True],
        [[[1, 3], [3, 0, 1], [2], [0]], False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.canVisitAllRooms(t[0])
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
