# https://leetcode.com/problems/fibonacci-number/


# Solution using two variables
#
# Runtime: 48 ms, faster than 54.58% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.8 MB, less than 54.34 % of Python3 online submissions for Fibonacci Number.


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        pp, p = 0, 1
        for _ in range(2, n+1):
            pp, p = p, p + pp
        return p


# Math solution fails for large numbers, fib(200) is short by 1
#
# Runtime: 52 ms, faster than 47.02% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 54.34 % of Python3 online submissions for Fibonacci Number.
class MathSolution:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** n + 1) / 5 ** 0.5)


# Solution using tabulation, O(n)
#
# Runtime: 67 ms, faster than 31.06% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.7 MB, less than 95.58 % of Python3 online submissions for Fibonacci Number.


class TSolution:
    def fib(self, n: int) -> int:
        f = [0 for _ in range(n + 2)]
        f[1] = 1
        for i in range(1, n):
            f[i+1] += f[i]
            f[i+2] += f[i]
        return f[n]


def test():
    sol = Solution()
    assert sol.fib(6) == 8
    assert sol.fib(20) == 6765
    assert sol.fib(50) == 12586269025
    assert sol.fib(200) == 280571172992510140037611932413038677189525


test()
