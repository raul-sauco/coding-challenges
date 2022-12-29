# 1108. Defanging an IP Address
# 🟢 Easy
#
# https://leetcode.com/problems/defanging-an-ip-address/
#
# Tags: String

import timeit

# 10e4 calls.
# » Loop                0.01319   seconds
# » SplitJoin           0.00581   seconds
# » StrReplace          0.00459   seconds


# Iterate over the characters in the input building the result, when we
# run into a "." we append the updated string.
#
# Time complexity: O(n) - We visit each character in the input once.
# Space complexity: O(1) - If we don't take into account the result str.
#
# Runtime 29 ms Beats 92.34%
# Memory 13.8 MB Beats 49.94%
class Loop:
    def defangIPaddr(self, address: str) -> str:
        res = []
        for c in address:
            if c == ".":
                res.append("[.]")
            else:
                res.append(c)
        return "".join(res)


# Split the string by "." then join using "[.]".
#
# Time complexity: O(n
# Space complexity: O(1)
#
# Runtime 41 ms Beats 64.28%
# Memory 13.7 MB Beats 99.93%
class SplitJoin:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))


# Use str.replace()
#
# Time complexity: O(n)
# Space complexity: O(1)
#
# Runtime 37 ms Beats 71.72%
# Memory 13.8 MB Beats 49.94%
class StrReplace:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


def test():
    executors = [
        Loop,
        SplitJoin,
        StrReplace,
    ]
    tests = [
        ["1.1.1.1", "1[.]1[.]1[.]1"],
        ["255.100.50.0", "255[.]100[.]50[.]0"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(10000):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.defangIPaddr(t[0])
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
