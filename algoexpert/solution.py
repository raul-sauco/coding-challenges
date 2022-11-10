# ####. Problem Name Here
# 🟢 Easy
# 🟠 Medium
# 🔴 Hard
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/problem-name
#
# Tags: ...

import timeit


# This is a template that can be used as the starting point of a
# solution with minimal changes.
class Solution:
    def methodCall(self, args: int) -> bool:
        pass


def test():
    executors = [Solution]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.methodCall(t[0])
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
