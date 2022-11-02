# 433. Minimum Genetic Mutation
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-genetic-mutation/
#
# Tags: Hash Table - String - Breadth-First Search

import timeit
from collections import deque
from typing import List

# This problem could be solved like Word Ladder, creating a dictionary
# of patterns: matches to save time finding neighbors, but given the
# small constrains of the description, it is doable, and simpler, to
# explore the entire bank searching for neighbors for each sequence that
# we visit.

# With the given input constrains, almost any approach is guaranteed to
# be efficient enough. This solution uses DFS, it checks the bank for
# any neighbors of the start word and recursively calls minMutation
# with that neighbor as the new start and having removed it from the
# list.
#
# Time complexity: O(m*n) - Where m is the number of characters in each
# sequence and n is the number of sequences, since they are both limited
# to 8 and 10 respectively, it is equivalent to O(80) - O(1).
# Space complexity: O(n) - The height of the call stack, limited to 10
# and so equivalent to O(1).
#
# Runtime: 34 ms, faster than 90.83%
# Memory Usage: 13.9 MB, less than 86.98%
class DFS:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # Base case match.
        if start == end:
            return 0
        # Base case fail.
        if end not in bank:
            return -1
        # Store the distances of all the ways we can arrive at end from
        # this sequence.
        distances = []
        # Iterate over the sequences in the bank to find the current
        # start neighbors and call minMutation with them.
        for i, sequence in enumerate(bank):
            dist = 0
            # Compute the number of differences.
            for a, b in zip(start, sequence):
                if a != b:
                    dist += 1
            if dist == 1:
                dist = self.minMutation(
                    sequence, end, bank[:i] + bank[i + 1 :]
                )
                if dist != -1:
                    distances.append(dist)
        if distances:
            return min(distances) + 1
        return -1


# We can also use BFS, which would become more and more efficient vs the
# DFS solution as the size of the input grows. Since we are trying to
# find a minimum distance between two nodes, and DFS will explore each
# branch all the way to the end before moving to the next branch, while
# BFS will explore all the nodes that we can reach at depth 1, then move
# to depth 2 and so on, stopping as soon as we arrive at the minimum
# distance. With a large enough input, it could be worth it to explore
# using BFS from both ends, which would improve performance and it is
# feasible given the problem.
#
# Time complexity: O(m*n) - Where m is the number of characters in each
# sequence and n is the number of sequences, since they are both limited
# to 8 and 10 respectively, it is equivalent to O(80) - O(1).
# Space complexity: O(n) - The height of the call stack, limited to 10
# and so equivalent to O(1).
#
# Runtime: 27 ms, faster than 98.8%
# Memory Usage: 13.8 MB, less than 86.98%
class BFS:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # Use a queue of mutation, number of mutations to reach it.
        q = deque([(start, 0)])
        seen = set(start)
        while q:
            current, steps = q.popleft()
            if current == end:
                return steps
            # Iterate over the sequences in the bank to find the current
            # start neighbors and call minMutation with them.
            for sequence in bank:
                if sequence not in seen:
                    dist = 0
                    # Compute the number of differences.
                    for i in range(8):
                        if current[i] != sequence[i]:
                            dist += 1
                        if dist > 1:
                            break
                    if dist == 1:
                        q.append((sequence, steps + 1))
                        seen.add(sequence)
        return -1


def test():
    executors = [
        DFS,
        BFS,
    ]
    tests = [
        ["AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1],
        ["AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2],
        ["AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minMutation(t[0], t[1], t[2])
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
