# 879. Profitable Schemes
# 🔴 Hard
#
# https://leetcode.com/problems/profitable-schemes/
#
# Tags: Array - Dynamic Programming

import json
import os
import timeit
from functools import cache
from typing import List


# Iterate over the indexes of the jobs, gang members and profit,
# computing the result of doing and skipping this job, if we go over
# the maximum allowed gang members, we return 0, this combination is
# not valid, if we reach the end of the array, we return 1 if we
# achieved the minimum profit and 0 if we didn't.
#
# Time complexity: O(n*mp*g) - Where n is the max number of gang members
# we can choose, mp is the minimum profit we need to make and g is the
# length of the profit and group arrays, these three are the ranges of
# the three parameters to the function that we are using to compute the
# results, since we are memoizing the function, that is the maximum
# number of times we may call it.
# Space complexity: O(n*mp*g) - The size of the cache, the call stack
# can grow to size g.
#
# Runtime 3903 ms Beats 26.67%
# Memory 682.3 MB Beats 5.71%
class Memoization:
    def profitableSchemes(
        self, n: int, minProfit: int, group: List[int], profit: List[int]
    ) -> int:
        # Explore the possibilities
        # idx: the index we are checking.
        # p: the profit up to that point.
        # g: the number of people pooled up to that point.
        # return: the number of profitable schemes of that branch.
        @cache
        def dfs(i: int, p: int, g: int) -> int:
            # Base case, we went over the group size limit.
            if g > n:
                return 0
            # Base case, we run out of indexes.
            if i == len(group):
                return int(p == minProfit)
            return dfs(
                i + 1, min(minProfit, p + profit[i]), g + group[i]
            ) + dfs(i + 1, p, g)

        # Return the result of the initial call.
        return dfs(0, 0, 0) % (10**9 + 7)


# TODO: add the dynamic programming solution.


def test():
    executors = [
        Memoization,
    ]
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    filename = os.path.splitext(os.path.basename(__file__))[0] + ".json"
    with open(os.path.join(__location__, filename)) as json_file:
        tests = json.load(json_file)
        for executor in executors:
            start = timeit.default_timer()
            for _ in range(1):
                for col, t in enumerate(tests):
                    sol = executor()
                    result = sol.profitableSchemes(t[0], t[1], t[2], t[3])
                    exp = t[4]
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
