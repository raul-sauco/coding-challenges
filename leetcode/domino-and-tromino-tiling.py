# 790. Domino and Tromino Tiling
# 🟠 Medium
#
# https://leetcode.com/problems/domino-and-tromino-tiling/
#
# Tags: Dynamic Programming

import timeit
from collections import deque


# We can see that the number of ways to place n tokens will be the
# same as the number of ways to place n-1 tokens with one more before
# and after it plus the ways to combine these two blocks, which is
# equivalent to the ways to place n-3 tokens. That means that, to
# compute the number of ways to place n tokens, we need to start with
# the known ways to place n=1, n=2, n=3 and keep computing higher values
# using these until we arrive at n. Since we only need the previous 3
# values at any point, we only need to store these, we can use a
# sliding window of values, implemented using a queue.
#
# Time complexity: O(n) - We only do one operation and push/pop into a
# queue at any given time.
# Space complexity: O(1) - We use constant space.
#
# Runtime 23 ms Beats 99.68%
# Memory 13.8 MB Beats 99.21%
class DP:
    def numTilings(self, n: int) -> int:
        q = deque([1, 2, 5])
        if n < 4:
            return q[n - 1]
        for _ in range(3, n):
            q.append(2 * q[-1] + q[0])
            q.popleft()
        return q[-1] % (10**9 + 7)


# Similar solution but avoiding the use of a queue.
#
# Time complexity: O(n) - We only do one operation and push/pop into a
# queue at any given time.
# Space complexity: O(1) - We use constant space.
#
# Runtime 34 ms Beats 94.76%
# Memory 13.8 MB Beats 99.21%
class DP2:
    def numTilings(self, n: int) -> int:
        dp = (1, 2, 5)
        if n < 4:
            return dp[n - 1]
        for _ in range(3, n):
            dp = (dp[1], dp[2], 2 * dp[-1] + dp[0])
        return dp[-1] % (10**9 + 7)


# Similar solution using 3 variables.
#
# Time complexity: O(n) - We only do one operation and push/pop into a
# queue at any given time.
# Space complexity: O(1) - We use constant space.
#
# Runtime 34 ms Beats 94.76%
# Memory 13.9 MB Beats 85.40%
class DP3:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        if n == 3:
            return 5
        a, b, c = 1, 2, 5
        for _ in range(3, n):
            a, b, c = b, c, 2 * c + a
        return c % (10**9 + 7)


def test():
    executors = [
        DP,
        DP2,
        DP3,
    ]
    tests = [
        [1, 1],
        [2, 2],
        [3, 5],
        [4, 11],
        [5, 24],
        [6, 53],
        [7, 117],
        [8, 258],
        [500, 603582422],
        [1000, 979232805],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numTilings(t[0])
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
