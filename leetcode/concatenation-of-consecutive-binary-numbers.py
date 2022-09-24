# 1680. Concatenation of Consecutive Binary Numbers
# 🟠 Medium
#
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
#
# Tags: Math - Bit Manipulation - Simulation

import timeit
from itertools import accumulate

# 1 call
# » OneLine             0.00264   seconds
# » ListComprehension   0.00313   seconds
# » BitCountIntSum      0.00229   seconds
# » MtrxMultiplication  0.00063   seconds
# » GeomProgression     0.00025   seconds
# » GemProg2            0.00013   seconds

# Use list comprehension and cast to string to generate the binary
# representation of the values 1..n then convert to int and modulo it.
#
# Time complexity: O(n) - Where n is the number of binary digits of the
# result string.
# Space complexity: O(n) - We need to generate a string of size n binary
# digits.
#
# Runtime: 2681 ms, faster than 51.97%
# Memory Usage: 23.9 MB, less than 14.17%
class OneLine:
    def concatenatedBinary(self, n: int) -> int:
        return int("".join([bin(x)[2:] for x in range(1, n + 1)]), 2) % (
            10**9 + 7
        )


# Use list comprehension and cast to string to generate the binary
# representation of the values 1..n then convert to int and modulo it.
#
# Time complexity: O(n) - Where n is the number of binary digits of the
# result string.
# Space complexity: O(n) - We need to generate a string of size n binary
# digits.
#
# Runtime: 2449 ms, faster than 55.91%
# Memory Usage: 15.9 MB, less than 22.05%
class ListComprehension:
    def concatenatedBinary(self, n: int) -> int:
        # Initialize a string result.
        s = ""
        # Iterate over 1..n
        for num in range(1, n + 1):
            # Add the binary representation of num to s.
            s += bin(num)[2:]
        # Convert s to int and modulo 10^9 + 7
        return int(s, 2) % (10**9 + 7)


# Iterate over the sequence 1..n, keeping track of the current result
# as an integer. For each value, calculate the number of bits of its
# binary representation, shift the result bits that many positions to
# the left and add the current value.
#
# Time complexity: O(n) - Where n is the number of values in the input.
# Space complexity: O(1) - We are only storing two integer values in
# memory.
#
# Runtime: 1524 ms, faster than 82.17%
# Memory Usage: 13.9 MB, less than 62.02%
class BitCountIntSum:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        # Initialize an int result.
        res = 0
        # Initialize the count of bits of the current number.
        bit_count = 0
        # Iterate over 1..n
        for num in range(1, n + 1):
            # Every time we find a power of 2, increase the bit count.
            if (num & (num - 1)) == 0:
                bit_count += 1
            # Shift the current bits of res left to accommodate the
            # number of bits of the coming value.
            res = ((res << bit_count) + num) % mod
        # Convert s to int and modulo 10^9 + 7
        return res


# TODO study the O(log(n)) solutions below.

# The next three solutions are not my own code, I added them here for
# completeness and to study them at a later point.

# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/discuss/963549/
class MtrxMultiplication:
    def concatenatedBinary(self, n: int) -> int:
        def multiply(X, Y):
            return [
                [
                    sum(a * b for a, b in zip(X_row, Y_col)) % 1000000007
                    for Y_col in zip(*Y)
                ]
                for X_row in X
            ]

        ans, acc, level = [[1], [2], [1]], 1, 1
        while acc < n:
            M = 2 ** (level + 1)

            # number of matrix production in this level
            x = take = min(n, M - 1) - acc
            mat = [[M, 1, 0], [0, 1, 1], [0, 0, 1]]

            # for example
            # num^13 = num * num^4 * num^8
            # num^6 = num^2 * num^4
            while x > 0:
                if x & 1:
                    ans = multiply(mat, ans)
                mat, x = multiply(mat, mat), x >> 1

            acc, level = acc + take, level + 1

        return ans[0][0]


# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/discuss/963886/
class GeomProgression:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7

        def modInverse(n):
            return pow(n, MOD - 2, MOD)

        def sumGeometricSeries(r, n):
            return (pow(r, n, MOD) - 1) * modInverse(r - 1)

        def sumBinaryOfLength(n, r):
            res = pow(2, n - 1, MOD) * sumGeometricSeries(
                pow(2, n, MOD), r - pow(2, n - 1, MOD) + 1
            )
            res %= MOD
            res += (
                sumGeometricSeries(pow(2, n, MOD), r - pow(2, n - 1, MOD) + 1)
                - 1
                - (r - pow(2, n - 1, MOD))
            ) * modInverse(pow(2, n, MOD) - 1)
            return res % MOD

        curr_size = 1
        res = 0
        for b in range(n.bit_length(), 0, -1):
            res += sumBinaryOfLength(b, min(n, pow(2, b) - 1)) * curr_size
            res %= MOD
            curr_size *= pow(
                2, (min(n, pow(2, b) - 1) - pow(2, b - 1) + 1) * b, MOD
            )
            curr_size %= MOD
        return (res + MOD) % MOD


# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/discuss/1037323/
#
# Time complexity: O(log^2 n)
# Space complexity; O(1) ?
#
# Runtime: 120 ms, faster than 99.22%
# Memory Usage: 13.8 MB, less than 79.84%
class GemProg2:
    def concatenatedBinary(self, n: int) -> int:
        def bin_pow(num):
            return [1 << i for i, b in enumerate(bin(num)[:1:-1]) if b == "1"]

        ans, MOD, q = 0, 10**9 + 7, len(bin(n)) - 3

        B = bin_pow((1 << q) - 1) + bin_pow(n - (1 << q) + 1)[::-1]
        C = list(range(1, q + 1)) + [q + 1] * (len(B) - q)
        D = list(accumulate(i * j for i, j in zip(B[::-1], C[::-1])))[::-1][
            1:
        ] + [0]

        for a, b, c, d in zip(accumulate(B), B, C, D):
            t1 = pow(2, b * c, MOD) - 1
            t2 = pow(pow(2, c, MOD) - 1, MOD - 2, MOD)
            ans += t2 * ((a - b + 1 + t2) * t1 - b) * pow(2, d, MOD)

        return ans % MOD


def test():
    executors = [
        OneLine,
        ListComprehension,
        BitCountIntSum,
        MtrxMultiplication,
        GeomProgression,
        GemProg2,
    ]
    tests = [
        [1, 1],
        [3, 27],
        [12, 505379714],
        [23032, 659725770],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.concatenatedBinary(t[0])
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
