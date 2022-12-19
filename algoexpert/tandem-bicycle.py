# Tandem Bicycle
# 🟢 Easy
#
# https://www.algoexpert.io/questions/tandem-bicycle
#
# Tags: Array - Greedy

import timeit
from itertools import accumulate


# We need to pair bikers depending on whether we want to optimize for
# speed or not, if we want the fastest speed, we need to pair faster
# bikers with slower ones, we can then sort one of the input arrays in
# reverse order. If we want the slower teams, then pair faster bikers
# with each other across teams.
#
# Time complexity: O(n*log(n)) - We will visit each element in the input
# twice, to sort and then to compute the result.
# Space complexity: O(n) - Sorting and the result list comprehension
# both have a linear space complexity.
class Solution:
    def tandemBicycle(self, redShirtSpeeds, blueShirtSpeeds, fastest):
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse=fastest)
        return sum(
            [
                max(redShirtSpeeds[i], blueShirtSpeeds[i])
                for i in range(len(blueShirtSpeeds))
            ]
        )


def test():
    executors = [Solution]
    tests = [
        [[5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True, 32],
        [[5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False, 25],
        [
            [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1],
            [3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32],
            True,
            816,
        ],
        [
            [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1],
            [3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32],
            False,
            484,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.tandemBicycle(t[0], t[1], t[2])
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
