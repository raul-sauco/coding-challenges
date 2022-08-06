# 458. Poor Pigs
# 🔴 Hard
#
# https://leetcode.com/problems/poor-pigs/
#
# Tags: Math - Dynamic Programming - Combinatorics

import timeit
from math import ceil, log


# We have minutesToTest // minutesToDie iterations, for each iteration
# we can split the buckets into pigs + 1, for example, if we only can
# test once and have 10 buckets, we can use 9 pigs, give each a bucket,
# if one of them dies, we know which bucket has the poison, if none of
# them do, the bucket we didn't use has the poison. We can use the same
# reasoning for a pile of buckets.
# We are then trying to find a number x such that, for each iteration
# available to us, we can divide the number of buckets by x + 1 and, at
# the end, we have a result <= 1
# The problem hints already give us a solution: x such that (T+1)^x >= N
#
# Time complexity: O(1) - It only computes two divisions and a log.
# Space complexity: O(1) - No extra space is used.
#
# Runtime: 56 ms, faster than 22.63%
# Memory Usage: 13.8 MB, less than 74.45%
class Math:
    def poorPigs(
        self, buckets: int, minutesToDie: int, minutesToTest: int
    ) -> int:
        # Base case
        if buckets < 2:
            return 0
        # Calculate the result.
        return ceil(log(buckets, minutesToTest / minutesToDie + 1))


# We can also find an iterative solution. The principle is the same as
# the above solution, we iterate over x values until x satisfies
# (T+1)^x >= N, then we return x.
#
# Time complexity: O(log(n)) - Each iteration we check buckets against
# the power of x.
# Space complexity: O(1) - Constant extra space.
#
# Runtime: 36 ms, faster than 81.75%
# Memory Usage: 14 MB, less than 20.44%
class Iterative:
    def poorPigs(
        self, buckets: int, minutesToDie: int, minutesToTest: int
    ) -> int:
        x = 0
        iterations = minutesToTest / minutesToDie + 1
        while iterations**x < buckets:
            x += 1
        return x


# We can improve the iterative solution if instead of calculating
# iterations**x at every step, we remember the previous value
# iterations^x-1 and we multiply once more by iterations.
# It should be possible to optimize even further if we obtained the
# most significant bit of iterations and used bit shifting with
# multiplication by a smaller number in each iteration.
#
# Time complexity: O(log(n)) - Each iteration we check buckets against
# the power of x.
# Space complexity: O(1) - Constant extra space.
#
# Runtime: 32 ms, faster than 92.70%
# Memory Usage: 13.9 MB, less than 74.45%
class DP:
    def poorPigs(
        self, buckets: int, minutesToDie: int, minutesToTest: int
    ) -> int:
        # Base case
        if buckets < 2:
            return 0
        x = 1
        iterations = minutesToTest / minutesToDie + 1
        res = iterations
        while res < buckets:
            res *= iterations
            x += 1
        return x


def test():
    executors = [Math, Iterative, DP]
    tests = [
        [1000, 15, 60, 5],
        [4, 15, 15, 2],
        [4, 15, 30, 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.poorPigs(t[0], t[1], t[2])
                exp = t[3]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
