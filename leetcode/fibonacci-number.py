# https://leetcode.com/problems/fibonacci-number/

import timeit


# Solution using two variables. Tabular dynamic programming.
#
# Runtime: 48 ms, faster than 54.58% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.8 MB, less than 54.34 % of Python3 online submissions for Fibonacci Number.

class DPTabVar:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a = b = 1
        for _ in range(n-1):
            a, b = b, a + b
        return a


# Math solution fails for large numbers, fib(200) is short by 1
#
# Runtime: 52 ms, faster than 47.02% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 54.34 % of Python3 online submissions for Fibonacci Number.
class Math:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return int((golden_ratio ** n + 1) / 5 ** 0.5)


# Solution using tabulation, O(n)
#
# Runtime: 67 ms, faster than 31.06% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.7 MB, less than 95.58 % of Python3 online submissions for Fibonacci Number.


class DPTab:
    def fib(self, n: int) -> int:
        f = [0 for _ in range(n + 2)]
        f[1] = 1
        for i in range(1, n):
            f[i+1] += f[i]
            f[i+2] += f[i]
        return f[n]


def test():
    executors = [DPTabVar,  DPTab, Math]
    tests = [
        [6, 8],
        [20, 6765],
        [50, 12586269025],
        # [200, 280571172992510140037611932413038677189525],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = executor()
                result = sol.fib(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
