# 2543. Check if Point Is Reachable
# 🔴 Hard
#
# https://leetcode.com/problems/check-if-point-is-reachable/
#
# Tags: Greedy - Dynamic Programming - Math

import timeit
from math import gcd


# Simulate the movements that are allowed but in reverse, starting at
# the target point and trying to reach (1, 1).
#
# Time complexity: O(log(max(m, n))) - At each step we divide by 2
# approximately, if one of the values is not divisible one loop, it will
# became divisible in the next loop.
# Space complexity: O(1) - We only store two integers and one tuple with
# two elements.
#
# Runtime 33 ms Beats 100%
# Memory 13.9 MB Beats 33.33%
class GreedySimulation:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        last, x, y = (-1, -1), targetX, targetY
        # While we make progress and have not matched the start.
        while (x, y) != last:
            if x == 1 and y == 1:
                return True
            last = (x, y)
            if x % 2 == 0:
                x //= 2
            if y % 2 == 0:
                y //= 2
            if x > y:
                x -= y
            if x < y:
                y -= x
        return False


# Great solutions using the greater common divisor in the discuss
# section. I liked one by lee215 in particular.
# https://leetcode.com/problems/check-if-point-is-reachable/solutions/3082073
#
# Time complexity: O(log(m) + log(y))
# Space complexity: O(1)
#
# Runtime 35 ms Beats 88.89%
# Memory 13.8 MB Beats 44.44%
class GCDPoT:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        mcd = gcd(targetX, targetY)
        return mcd == mcd & -mcd


def test():
    executors = [
        GreedySimulation,
        GCDPoT,
    ]
    tests = [
        [6, 9, False],
        [4, 7, True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isReachable(t[0], t[1])
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
