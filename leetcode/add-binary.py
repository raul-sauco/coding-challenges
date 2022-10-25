# 67. Add Binary
# 🟢 Easy
#
# https://leetcode.com/problems/add-binary/
#
# Tags: Math - String - Bit Manipulation - Simulation

import timeit


# Iterate over both strings from the bits of least weight to the bits of
# most weight adding them into a result.
#
# Time complexity: O(max(m,n)) - Where m and n are the lengths of a and
# b, we will iterate as many times as characters on the longest input
# string.
# Space complexity: O(max(m,n)) - The list of resulting bits will have
# as many elements as digits on the longest input string plus possibly
# one more.
#
# Runtime: 76 ms, faster than 18.20%
# Memory Usage: 13.9 MB, less than 25.36%
class ByPosition:
    def addBinary(self, a: str, b: str) -> str:
        bits = []
        # Get the last index of each string.
        i, j = len(a) - 1, len(b) - 1
        # Initialize the carry to 0.
        carry = 0
        # Iterate while we haven't visited both strings first digit at 0.
        while i >= 0 or j >= 0:
            # Initialize the result at 0 or 1.
            res = carry
            # If we still have digits to visit in a.
            if i >= 0 and a[i] == "1":
                res += 1
            # If we still have digits to visit in b.
            if j >= 0 and b[j] == "1":
                res += 1
            i -= 1
            j -= 1
            carry = 1 if res > 1 else 0
            bits.append("1" if res == 1 or res == 3 else "0")
        # Check if we have a carry leftover from the highest order digits.
        if carry:
            bits.append("1")
        return "".join(reversed(bits))


# Use binary xor to compute the sum of the numbers and binary and to
# compute the carry, keep adding the numbers while we have a carry.
#
# Time complexity: log(max(a, b)) - The carry operation will happen at
# most n times where n is the number of bits in the longest of the two
# inputs.
# Space complexity: O(1) - The only additional space we use is to store
# two integer values.
#
# Runtime: 61 ms, faster than 53.12%
# Memory Usage: 13.9 MB, less than 72.50%
class XorAnd:
    def addBinary(self, a: str, b: str) -> str:
        # Cast the input strings to integers.
        res, carry = int(a, 2), int(b, 2)
        while carry:
            res, carry = res ^ carry, (res & carry) << 1
        # Convert int to binary string.
        # https://stackoverflow.com/a/699891/2557030
        return "{0:b}".format(res)
        # Another method would be to use bin()
        # https://stackoverflow.com/a/699892/2557030
        # return str(bin(res))[2:]


# If we are allowed to cast the values this problem becomes trivial,
# cast the values to integers, add them and cast the result to string.
#
# Time complexity: O(1) ??
# Space complexity: O(1) - The only extra memory is two integers.
#
# Runtime: 47 ms, faster than 77.06%
# Memory Usage: 13.9 MB, less than 25.36%
class Casting:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]


def test():
    executors = [
        ByPosition,
        XorAnd,
        Casting,
    ]
    tests = [
        ["0", "0", "0"],
        ["1", "1", "10"],
        ["0", "10", "10"],
        ["11", "1", "100"],
        ["1010", "1011", "10101"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.addBinary(t[0], t[1])
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
