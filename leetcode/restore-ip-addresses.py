# 93. Restore IP Addresses
# 🟠 Medium
#
# https://leetcode.com/problems/restore-ip-addresses/
#
# Tags: String - Backtracking

import timeit
from typing import List


# Use backtracking a pointer to the index in the input string that we
# are processing and integers to represent the bytes of the IP to build
# all the possible IPs one byte at a time ignoring combinations that are
# not valid. This solution improves on most of the other recursive
# solutions by avoiding slicing the input string and copying it in each
# function call.
#
# Time complexity: O(2^n) - The recursive tree may split in two at each
# digit on the input.
# Space complexity: O(2^n) - With the right input, we could have 2^n
# number of valid IP addresses that we store in res.
#
# Runtime 25 ms Beats 99.35%
# Memory 13.8 MB Beats 79.81%
class RecursiveBT:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, ip, n = [], [int(s[0])], len(s)
        # A recursive function that uses backtracking to efficiently
        # try the digit at index i as both the last digit of the current
        # byte and the first digit of the next byte.
        def bt(i: int):
            # Base case, we have added too many bytes or there aren't
            # enough digits left to construct a 4 byte ip.
            if len(ip) > 4 or n - i + len(ip) < 4:
                return
            # Base case, we consumed the input string.
            if i == n:
                if len(ip) == 4:
                    res.append(".".join(map(str, ip)))
                return
            digit = int(s[i])
            byte = ip[-1]
            # Option one, try to add this digit to the current byte.
            new_byte = byte * 10 + digit
            if new_byte != digit and new_byte < 256:
                ip[-1] = new_byte
                bt(i + 1)
                ip[-1] = byte
            # Always move forward closing the current byte.
            ip.append(digit)
            bt(i + 1)
            ip.pop()

        bt(1)
        return res


# An iterative solution, have 3 nested loops that compute the index
# before which we want to insert the dots, if the resulting bytes are
# valid, it adds the result to the solution.
#
# Time complexity: O(1) - There are three nested loops any of which can
# tries 3 different values that is O(3^3) which simplifies to O(1).
# Space complexity: O(2^n) - With the right input, we could have 2^n
# number of valid IP addresses that we store in res.
#
# Runtime 28 ms Beats 97.86%
# Memory 13.8 MB Beats 79.81%
class Iterative:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        limit = 255
        for i in range(1, 4):
            byte1 = s[:i]
            if int(byte1) > limit or (byte1[0] == "0" and len(byte1) > 1):
                break
            for j in range(i + 1, i + 4):
                if j > len(s) - 2:
                    break
                byte2 = s[i:j]
                if int(byte2) > limit or (byte2[0] == "0" and len(byte2) > 1):
                    break
                for k in range(j + 1, j + 4):
                    if not (len(s) - 4 < k < len(s)):
                        continue
                    byte3 = s[j:k]
                    if int(byte3) > limit or (
                        byte3[0] == "0" and len(byte3) > 1
                    ):
                        continue
                    byte4 = s[k:]
                    if int(byte4) > limit or (
                        byte4[0] == "0" and len(byte4) > 1
                    ):
                        continue
                    res.append(".".join([byte1, byte2, byte3, byte4]))
        return res


def test():
    executors = [
        RecursiveBT,
        Iterative,
    ]
    tests = [
        ["000256", []],
        ["0000", ["0.0.0.0"]],
        ["25525511135", ["255.255.11.135", "255.255.111.35"]],
        [
            "101023",
            ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.restoreIpAddresses(t[0])
                exp = t[1]
                assert sorted(result) == sorted(exp), (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
