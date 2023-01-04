# 2244. Minimum Rounds to Complete All Tasks
# 🟠 Medium
#
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
#
# Tags: Array - Hash Table - Greedy - Counting

import timeit
from collections import Counter
from typing import List


# We need to count the number of tasks of each difficulty, then greedily
# group them in as many groups of 3 as possible with 0, 1 or 2 groups of
# 2 at the end to place the remainder of freq % 3 if any. We can use
# Counter to group the tasks by difficulty, then divide by 3 to obtain
# the number of groups, if there is any remainder to the division, we
# need to add one more group to the result.
#
# Time complexity: O(n) - We visit each element once, then iterate over
# the frequencies that will be, at most n.
# Space complexity: O(n) - The counter can grow in size with the input.
#
# Runtime 2133 ms Beats 44.76%
# Memory 28.4 MB Beats 44.10%
class UseDivMod:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequencies = Counter(tasks)
        res = 0
        for frequency in frequencies.values():
            if frequency == 1:
                return -1
            q, rem = divmod(frequency, 3)
            res += q
            if rem:
                res += 1
        return res


# Improve the previous solution using the division operation instead of
# a call to divmod.
#
# Time complexity: O(n) - We visit each element once, then iterate over
# the frequencies that will be, at most n.
# Space complexity: O(n) - The counter can grow in size with the input.
#
# Runtime 1220 ms Beats 57.87%
# Memory 28.2 MB Beats 82.79%
class AddTwo:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequencies = Counter(tasks)
        res = 0
        for freq in frequencies.values():
            if freq == 1:
                return -1
            res += (freq + 2) // 3
        return res


# Same logic as the previous solution but condensed into two lines, one
# to instantiate the counter, one to get the result.
#
# Time complexity: O(n) - We visit each element once, then iterate over
# the frequencies that will be, at most n.
# Space complexity: O(n) - The counter can grow in size with the input.
#
# Runtime 1779 ms Beats 48.4%
# Memory 28.3 MB Beats 70.66%
class Shorter:
    def minimumRounds(self, tasks: List[int]) -> int:
        frequencies = Counter(tasks).values()
        return (
            -1
            if 1 in frequencies
            else sum((freq + 2) // 3 for freq in frequencies)
        )


def test():
    executors = [
        UseDivMod,
        AddTwo,
        Shorter,
    ]
    tests = [
        [[2, 3, 3], -1],
        [[2, 2, 3, 3, 2, 4, 4, 4, 4, 4], 4],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimumRounds(t[0])
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
