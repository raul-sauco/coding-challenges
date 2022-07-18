# https://leetcode.com/problems/number-of-1-bits/

# Tags: Array - Math

import timeit


# Shift bits and check if the last bit is a 1
# https://stackoverflow.com/a/13522788/2557030
#
# Time complexity: O(log(n))
# Space complexity: O(1)
#
# Runtime: 41 ms, faster than 69.96% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 13.8 MB, less than 50.25% of Python3 online submissions for Number of 1 Bits.
class CountBits:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        while n:
            # Add one if the last bit is even
            if n % 2 == 1:
                ones += 1
            # Shift bits to the right
            n >>= 1
        return ones


# Use the bit_count method added in python 3.10.
#
# Runtime: 37 ms, faster than 81.43% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 14 MB, less than 7.72% of Python3 online submissions for Number of 1 Bits.
class BuiltIn:
    def hammingWeight(self, n: int) -> int:
        # Needs python >= 3.10
        return n.bit_count()


def test():
    executors = [CountBits, BuiltIn]
    tests = [
        [0, 0],
        [11, 3],
        [128, 1],
        [4294967293, 31],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.hammingWeight(t[0])
                exp = t[1]
                assert result == exp, f"\033[93m» {t[0]} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
