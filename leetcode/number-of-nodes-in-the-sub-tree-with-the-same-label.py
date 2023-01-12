# 1519. Number of Nodes in the Sub-Tree With the Same Label
# 🟠 Medium
#
# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
#
# Tags: Hash Table - Tree - Depth-First Search - Breadth-First Search - Counting

import timeit
from collections import Counter
from typing import List


# Create an adjacency list of the given graph that we know is a tree,
# use the list to do a depth first search where nodes return the
# frequencies of labels in the subtree that they are the root of, a
# parent adds its own label to the frequencies of all children, uses
# the counter to obtain the frequency of its own label and update the
# result array with it and returns the frequency counter to its parent.
#
# Time complexity: O(n) - Each node is visited once, for each visit, we
# do O(1) operations.
# Space complexity: O(n) - The call stack will grow to the height of the
# tree, which could be n, each call receives 2 parameters and returns a
# dictionary of max size 26.
#
# Runtime 3041 ms Beats 74.36%
# Memory 192.2 MB Beats 50.64%
class Solution:
    def countSubTrees(
        self, n: int, edges: List[List[int]], labels: str
    ) -> List[int]:
        # Construct and adjacency list.
        neighbors = [[] for _ in range(n)]
        res = [None] * n
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        # A DFS function that computes the number of labels in a tree.
        def dfs(node, parent):
            # Compute the frequencies of all labels in this subtree.
            freq = Counter([labels[node]])
            # Visit all children. Avoid visiting the parent.
            for child in neighbors[node]:
                if child == parent:
                    continue
                freq += dfs(child, node)
            # The answer for this node is its label's frequency.
            res[node] = freq[labels[node]]
            # Return all the frequencies so nodes higher up in the tree
            # can compute their own results.
            return freq

        dfs(0, -1)
        return res


def test():
    executors = [Solution]
    tests = [
        [4, [[0, 1], [1, 2], [0, 3]], "bbbb", [4, 2, 1, 1]],
        [5, [[0, 1], [0, 2], [1, 3], [0, 4]], "aabab", [3, 2, 1, 1, 1]],
        [
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            "abaedcd",
            [2, 1, 1, 1, 1, 1, 1],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countSubTrees(t[0], t[1], t[2])
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
