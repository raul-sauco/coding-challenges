# Minimum Waiting Time
# 🟢 Easy
#
# https://www.algoexpert.io/questions/minimum-waiting-time
#
# Tags: Greedy Algorithms

import timeit
from typing import List


# Iterate over the sorted queries computing the total linear waiting
# time of the queries run up to that point, each query has been waiting
# that amount of time, add its waiting time to the combined waiting time
# of all queries. Since the queries are sorted, the longest query will
# be the one that we want to run last, we want to execute faster queries
# earlier to minimize the waiting time.
#
# Time complexity: O(n*log(n)) - Sorting has the highest complexity.
# Space complexity: O(n) - Sorting in python takes up to n/2 memory in
# the worst case, even though is O(1) in the best case.
class Solution:
    def minimumWaitingTime(self, queries: List[int]) -> int:
        total = cumulative = last = 0
        for query in sorted(queries):
            cumulative += last
            total += cumulative
            last = query
        return total


def test():
    executors = [Solution]
    tests = [
        [[12], 0],
        [[12, 3], 3],
        [[3, 2, 1, 2, 6], 17],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minimumWaitingTime(t[0])
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
