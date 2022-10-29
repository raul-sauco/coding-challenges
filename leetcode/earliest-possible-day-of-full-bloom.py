# 2136. Earliest Possible Day of Full Bloom
# 🔴 Hard
#
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
#
# Tags: Array - Greedy - Sorting

import timeit
from operator import itemgetter
from typing import List


# We want to make sure that we are doing something else while the plants
# are growing, we can start planting the ones that will take the longest
# time to bloom once planted, then, while we "wait" for them, we can
# get busy and keep planting the next ones.
#
# Time complexity: O(n*log(n)) - For the sorting.
# Space complexity: O(n) - Sorting takes O(n) in the worst case.
#
# Runtime: 4402 ms, faster than 26.22%
# Memory Usage: 31.7 MB, less than 58.58%
class Greedy:
    def earliestFullBloom(
        self, plantTime: List[int], growTime: List[int]
    ) -> int:
        # Store the day at which the last blooming plant blooms and the
        # next day at which we can start planting.
        res = can_plant = 0
        # Iterate over the plants sorted by decreasing growth time.
        for pt, gt in sorted(
            zip(plantTime, growTime), key=itemgetter(1), reverse=True
        ):
            # Plant this plant as soon as possible, if it would bloom
            # after the latest bloom seen, this is the new result.
            res = max(res, can_plant + pt + gt)
            can_plant += pt
        return res


def test():
    executors = [Greedy]
    tests = [
        [[1, 4, 3], [2, 3, 1], 9],
        [[1, 2, 3, 2], [2, 1, 2, 1], 9],
        [[1], [1], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.earliestFullBloom(t[0], t[1])
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
