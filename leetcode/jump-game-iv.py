# 1345. Jump Game IV
# 🔴 Hard
#
# https://leetcode.com/problems/jump-game-iv/
#
# Tags: Array - Hash Table - Breadth-First Search

import json
import os
import timeit
from collections import defaultdict, deque
from typing import List


# What we have is a connected undirected graph where we can use the
# element indexes as the vertex identifiers, we want to go from 0 to n-1
# in the minimum number of steps possible, we can use breadth-first
# search, to prepare for it, we can first create an adjacency list,
# each node's neighbors are the vertices before and after, and any other
# vertices with the same value.
#
# Time complexity: O(n) - We have three sections that visit each element
# on the input array and do constant work.
# Space complexity: O(n) - There are several data structures that take
# n memory.
#
# Runtime 670 ms Beats 96.59%
# Memory 27.7 MB Beats 91.87%
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # Base case.
        if n < 2:
            return 0
        # A dictionary of vertices indexed by values.
        d = defaultdict(list)
        for i in reversed(range(n)):
            d[arr[i]].append(i)
        # A function that gets all neighbors of a node that we have not
        # queued yet.
        def getUnqueuedNeighbors(i: int) -> List[int]:
            adj = []
            # We can reach the element before.
            if 0 < i and not seen[i - 1]:
                seen[i - 1] = True
                adj.append(i - 1)
            # We can reach the element after.
            if i < n - 1 and not seen[i + 1]:
                seen[i + 1] = True
                adj.append(i + 1)
            # We can also reach any element with the same value.
            if arr[i] in d:
                for node in d[arr[i]]:
                    if node != i:
                        adj.append(node)
                        seen[node] = True
                d.pop(arr[i])
            return adj

        # A list of nodes that we have visited already.
        seen = [False] * n
        seen[0] = True
        # BFS starting at 0 and counting the steps until we reach n-1.
        steps, level = 0, deque([0])
        while level:
            steps += 1
            # Process an entire level.
            for _ in range(len(level)):
                current = level.popleft()
                for nei in getUnqueuedNeighbors(current):
                    # If this is the target node, return.
                    if nei == n - 1:
                        return steps
                    level.append(nei)
        raise Exception("Unreachable code")


def test():
    executors = [Solution]
    # The tests are big, use a separate JSON file.
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "jump-game-iv.json")) as json_file:
        tests = json.load(json_file)
        for executor in executors:
            start = timeit.default_timer()
            for _ in range(1):
                for col, t in enumerate(tests):
                    sol = executor()
                    result = sol.minJumps(t["arr"])
                    exp = t["res"]
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
