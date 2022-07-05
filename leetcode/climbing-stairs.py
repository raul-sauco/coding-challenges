# https://leetcode.com/problems/climbing-stairs/

# Intuition, I can reach each step from n-1 and n-2, add the ways to reach them
# It is a fibonacci sequence
import timeit

# Runtime: 42 ms, faster than 59.35% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 13.8 MB, less than 57.08 % of Python3 online submissions for Climbing Stairs.


class Solution:
    def climbStairs(self, n: int) -> int:
        # Between 0 and 2, return the value itself
        if n < 3:
            return n
        # Initialize pointers with the seeds
        pp, p = 1, 1
        # Iterate from 2 to n-1
        for _ in range(n):
            # Increase the values of the next table positions
            # 0 1 2 3 5 8 13 ...
            pp, p = p, p + pp
        # Return the memoized value of adding up n-1 + n-2 up to n
        return pp


def test():
    executors = [
        {'executor': Solution, 'title': 'Solution', },
    ]
    tests = [
        [0, 0],
        [1, 1],
        [2, 2],
        [3, 3],
        [5, 8],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = executor['executor']()
                result = sol.climbStairs(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(
            executor['title'], used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
