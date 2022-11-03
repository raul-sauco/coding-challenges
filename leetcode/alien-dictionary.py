# 269. Alien Dictionary
# 🔴 Hard
#
# https://leetcode.com/problems/alien-dictionary/
# https://www.lintcode.com/problem/892/
#
# Tags: Array - Breadth First Search/BFS - Topological Sort

import timeit
from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List


# Iterate over all characters in the input and add them to a set, then
# iterate over each pair of words until we find the one ordering
# relation that each can provide, use that relation to add two entries
# to an indegree and outdegree dictionaries. Also pop any characters
# that have dependencies from the set of all characters. On the second
# half of the algorithm, we heapify the set of all characters and use
# it as the queue for our BFS, we pop characters from it and iterate
# over their dependencies removing the current character. Any
# dependent that sees all its dependencies removed is added to the heap.
#
# Time complexity: O(m*n) - Where m is the number of words and n is
# the average length of the words. We iterate over all words at O(m) and
# check the characters at the same index O(n).
# Space complexity: O(m*n) - We store the input in several structures.
#
# Runtime: 122 ms, faster than 16.80% on LintCode.
# Memory Usage: 6.88 MB, less than 16.80%
class UseHeap:
    def alienOrder(self, words: List[str]) -> str:
        all_chars = {c for word in words for c in word}
        # A dictionary of characters with the characters that we know
        # come after them in alien order.
        followed_by = defaultdict(set)
        # A dictionary of characters with the number of characters that
        # we know do come before them in the alien order.
        preceded_by = defaultdict(set)
        # Iterate over each pair of words.
        for j in range(1, len(words)):
            i = j - 1
            k = 0
            while k < len(words[i]) or k < len(words[j]):
                # If the characters to k where the same and words[i]
                # is longer, it should be after words[j] in the
                # input, the dictionary is not valid.
                if len(words[j]) <= k:
                    return ""
                if (
                    k < len(words[i])
                    and k < len(words[j])
                    and words[i][k] != words[j][k]
                ):
                    followed_by[words[i][k]].add(words[j][k])
                    preceded_by[words[j][k]].add(words[i][k])
                    # Remove any characters that go after another
                    # from the all chars set.
                    if words[j][k] in all_chars:
                        all_chars.remove(words[j][k])
                    break
                k += 1
        # Store the result.
        res = []
        # Use a heap to get the min character in O(log(n))
        heap = list(all_chars)
        heapify(heap)
        while heap:
            lowest = heappop(heap)
            res.append(lowest)
            for dependent in followed_by[lowest]:
                preceded_by[dependent].remove(lowest)
                if not preceded_by[dependent]:
                    preceded_by.pop(dependent)
                    heappush(heap, dependent)
        # If we could not satisfy some of the dependencies, the
        # dictionary is invalid.
        if preceded_by:
            return ""
        return "".join(res)


# The DFS solution by NeetCode is much more efficient on the tests even
# when it takes more time locally. It is also a neat idea!
#
# https://github.com/neetcode-gh/leetcode/blob/main/python/269-Alien-Dictionary.py
#
# Use the clues in the input to build a graph of chars -> set(higher
# lexicographical order chars), then do DFS from each root char key
# creating a list of the lexicographically ordered characters (in alien
# order first then latin order). Use a visit dictionary for a double
# purpose, mark characters as false once we have processed them and as
# true when they are part of the current path that we are exploring on
# the depth-first search. If we ever try to process a character that
# is marked as true, we have found a cycle and we can return "".
#
# Time complexity: O(m*n) - Where m*n is the number of characters in the
# input. This comes from the first part of the algorithm where we build
# the adjacency list, the second part of the algorithm, the depth-first
# search, runs on O(1) because it will be called a max of 26 times, when
# we call it for a character that we have processed already, it will
# immediately return the stored result.
# Space complexity: O(1) - The call stack could be as deep as the number
# of keys in adj, that number also is the number of unique characters in
# the input and it maxes at 26. O(26) => O(1).
#
# Runtime: 81 ms, faster than 99.20% on LintCode.
# Memory Usage: 6.05 MB, less than 99.20%
class DFS:
    def alienOrder(self, words: List[str]) -> str:
        # First part: construct adjacency list from input.
        # Create a dictionary of char: set of higher order chars.
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # If we find a contradiction.
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        # Second part: construct result from adjacency list.
        # Use a set to detect cycles and an array for the result.
        visit = {}
        res = []
        # DFS from each non-dependent start character.
        def dfs(c):
            if c in visit:
                return visit[c]
            # Mark c as belonging to the path that we are currently
            # exploring.
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            # If there are no cycles detected, add this char to the
            # result after its dependents. Will reverse before return.
            res.append(c)
            # Mark this node as processed.
            visit[c] = False

        # Iterate over neighbors in sorted order. Needed for LintCode
        # requirement of secondary latin lexicographical order.
        for ch in sorted(adj.keys(), reverse=True):
            if dfs(ch):
                return ""
        res.reverse()
        return "".join(res)


def test():
    executors = [
        UseHeap,
        DFS,
    ]
    tests = [
        [["aba"], "ab"],
        [["z", "z"], "z"],
        [["z", "x"], "zx"],
        [["abc", "ab"], ""],
        [["zy", "zx"], "yxz"],
        [["ab", "adc"], "abcd"],
        [["a", "ba", "bc", "c"], "abc"],
        [["abc", "bcd", "qwert", "ab"], ""],
        [["wrt", "wrf", "er", "ett", "rftt"], "wertf"],
        [["wrt", "wrf", "er", "ett", "rftt", "te"], "wertf"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.alienOrder(t[0])
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
