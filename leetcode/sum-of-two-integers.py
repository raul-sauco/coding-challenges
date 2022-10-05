# 371. Sum of Two Integers
# 🟠 Medium
#
# https://leetcode.com/problems/sum-of-two-integers/
#
# Tags: Math - Bit Manipulation

import timeit

# 10e4 calls
# » Iterative           0.13291   seconds
# » Recursive           0.23407   seconds


# Use bitwise XOR to sum the two number's bits.
#
# 11001011 ^
#    11001
# --------
# 11010010
#
# Use the result of bitwise AND shifted 1 bit to the left to represent
# the sum's carry.
#
# 11001011 &, << 1
#    11001
# --------
# 00010010
#
# Keep computing while we have a carry to add to the sum.

# Time and space complexity are bounded because the problem description
# guarantees that -1000 <= a, b <= 1000. => O(1)

# Time complexity: O(1)
# Space complexity: O(1)
#
# Runtime: 32 ms, faster than 91.47%
# Memory Usage: 13.9 MB, less than 14.63%
class Iterative:
    def getSum(self, a: int, b: int) -> int:
        # The problem guarantees -1000 <= a, b <= 1000
        MAX = 0x7FFFFFFF
        # Mask of 32 1s.
        mask = 0xFFFFFFFF
        # Keep iterating while the carry is not null.
        while b:
            # Use a to store the sum, using XOR of the bits of a and b.
            # Use b to store the carry, using AND shifted one position
            # to the left, of the sum of a and b. Because of Python's
            # unbounded integers, we need to use a mask of the maximum
            # expected integer size. Discard bits greater than the mask.
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= MAX else ~(a ^ mask)


# Time complexity: O(1)
# Space complexity: O(1)
#
# Runtime: 49 ms, faster than 54.87%
# Memory Usage: 13.9 MB, less than 62.25%
class Recursive:
    def __init__(self) -> None:
        # The problem guarantees a, b < 2^32
        self.MAX = 0x7FFFFFFF
        # Mask of 32 1s.
        self.MASK = 0xFFFFFFFF

    def getSum(self, a: int, b: int) -> int:
        if not b:
            return a if a <= self.MAX else ~(a ^ self.MASK)
        return self.getSum((a ^ b) & self.MASK, ((a & b) << 1) & self.MASK)


def test():
    executors = [
        Iterative,
        Recursive,
    ]
    tests = [
        [0, 0, 0],
        [1, 2, 3],
        [2, 3, 5],
        [2, -2, 0],
        [-2, 2, 0],
        [3, -3, 0],
        [16, -14, 2],
        [-2, -2, -4],
        [-11, 0, -11],
        [-12, -8, -20],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.getSum(t[0], t[1])
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
