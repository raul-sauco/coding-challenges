# 2246. Longest Path With Different Adjacent Characters
# 🔴 Hard
#
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
#
# Tags: Array - String - Tree - Depth-First Search - Graph - Topological Sort

import collections
import timeit
from typing import List


# Explore the tree using depth-first search, each node computes two
# maximum path values, the longest path that has this node as part of
# the path, and the longest path that uses this node as a root, we
# return the first value to the parent, together with the character at
# the node, and use the second to update a global max path value.
#
# Time complexity: O(n) - We will visit each node once.
# Space complexity: O(n) - The call stack will grow to the height of the
# tree, which could be n.
#
# Runtime 1757 ms Beats 88.6%
# Memory 151 MB Beats 62.15%
class DFS:
    def longestPath(self, parent: List[int], s: str) -> int:
        # Create an adjacency list of children.
        children = [[] for _ in range(len(parent))]
        for c, p in enumerate(parent):
            if p >= 0:
                children[p].append(c)
        # Initialize the longest overall path seen.
        longest = 0

        def dfs(node) -> int:
            nonlocal longest
            # The two longest paths returned from this nodes children.
            lp = [0, 0]
            for child in children[node]:
                # Always call dfs on the child, even if the path is
                # not useful to the parent, the longest path may be in
                # the subtree that has that child as root.
                length = dfs(child)
                if s[node] == s[child]:
                    continue
                # If the labels are different, update longest paths.
                if lp[1] < length:
                    lp[1] = length
                if lp[0] < lp[1]:
                    lp[0], lp[1] = lp[1], lp[0]
            # The longest path seen could be rooted at this node.
            longest = max(longest, sum(lp) + 1)
            # The longest path through this node would go down the
            # single longest child path.
            return lp[0] + 1

        # Initial call.
        dfs(0)
        # Return the longest path with no adjacent same characters.
        return longest


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = collections.defaultdict(set)
        for i, ele in enumerate(parent):
            if i == 0:
                continue
            tree[ele].add(i)
        self.ans = 1

        def dfs(node):
            child = []
            for v in tree[node]:
                length = dfs(v)
                if s[v] != s[node]:
                    child.append(length)
            child.sort(reverse=True)
            res = 1
            for i in range(2):
                if i == len(child):
                    break
                res += child[i]
            self.ans = max(self.ans, res)
            return 1 + (child[0] if child else 0)

        dfs(0)
        return self.ans


def test():
    executors = [DFS, Solution]
    tests = [
        [[-1, 0, 0, 1, 1, 2], "abacbe", 3],
        [[-1, 0, 0, 0], "aabc", 3],
        [[-1, 0, 1], "aab", 2],
        [[-1, 0, 0, 1, 2, 2, 4, 5, 7], "aabaccdde", 6],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestPath(t[0], t[1])
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
