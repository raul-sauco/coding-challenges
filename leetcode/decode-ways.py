# 91. Decode Ways
# 🟠 Medium
#
# https://leetcode.com/problems/decode-ways/
#
# Tags: String - Dynamic Programming

import timeit


# Time complexity: O(2^n) - The worst case complexity would happen if
# every number could be used as the first and second digit of a multi
# digit encoding. In that case, at each step, the decision tree would
# split in two.
#
# TODO Add the brute force solution.
class BruteForce:
    def numDecodings(self, s: str) -> int:
        pass


# We can iterate over the input storing the number of ways to decode up
# to the current position. dp[x] will be dp[x-1]+dp[x-2] when the two
# last values can be used to construct a multi-digit encoding, otherwise
# dp[x-1] because we are not adding any branches to the decision tree.
# We need to be careful handling the several special cases that happen
# around the value 0.
#
# Time complexity: O(n) - The worst case complexity would happen if
# every number could be used as the first and second digit of a multi
# digit encoding. In that case, at each step, the decision tree would
# split in two.
# Space complexity: O(n) - The dp array has the same size as the input.
# Since we are only interested in the two previous values at most, it
# would be easy to update the logic to only store the two previous
# solutions at O(1)
#
# Runtime: 61 ms, faster than 37.59%
# Memory Usage: 13.7 MB, less than 98.57%
class DP:
    def numDecodings(self, s: str) -> int:
        # Base case, invalid input.
        if s[0] == "0":
            return 0
        # Base case short string.
        if len(s) == 1:
            return 1
        dp = [1, 1] + [0] * (len(s) - 1)
        # Define a function that determines if two digits can be split
        # or can only work together.
        def valid(a: str, b: str) -> bool:
            return (a == "1" and b in "123456789") or (
                a == "2" and b in "123456"
            )

        for i in range(2, len(s) + 1):
            # If at any point we find a non-decodable sequence return 0.
            if s[i - 1] == "0" and s[i - 2] in "34567890":
                return 0
            if valid(s[i - 2], s[i - 1]) and not (i < len(s) and s[i] == "0"):
                # If there is a next character and it is a 0, we may
                # need to use this character to build a string with it.
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


# We can iterate over the input storing the number of ways to decode up
# to the current position. `next` will be `prev`+`curr` when the two
# last values can be used to construct a multi-digit encoding, otherwise
# `curr` because we are not adding any branches to the decision tree.
# We need to be careful handling the several special cases that happen
# around the value 0.
#
# Time complexity: O(n) - The worst case complexity would happen if
# every number could be used as the first and second digit of a multi
# digit encoding. In that case, at each step, the decision tree would
# split in two.
# Space complexity: O(1) - Since we are only interested in the two
# previous values at most, it is easy to update the logic to only store
# the two previous values, reducing the memory complexity to O(1)
#
# Runtime: 33 ms, faster than 94.18%
# Memory Usage: 13.9 MB, less than 80.35%
class O1DP:
    def numDecodings(self, s: str) -> int:
        # Base case, invalid input.
        if s[0] == "0":
            return 0
        # Base case short string.
        if len(s) == 1:
            return 1
        # Store the two previous dp values.
        prev, curr = 1, 1
        # Iterate over the input
        for i in range(1, len(s)):
            # Store the current and next digits in variables.
            a, b = s[i - 1], s[i]
            # If at any point we find a non-decodable sequence return 0.
            if b == "0" and a in "34567890":
                return 0
            # If the combination is valid, it will always have, at
            # least as many ways to combine it as the previous position,
            # in this case, we are just adding this letter to the
            # result.
            next = curr
            # If the current and next values can work together as well
            # as independently and the next value is not a 0 (which
            # would require current to always go with it) Then we need
            # to add as many ways as there were to form the previous
            # decode as well, we may choose to use the current value
            # independently or to form a pair.
            if (
                (a == "1" and b in "123456789") or (a == "2" and b in "123456")
            ) and not (i < len(s) - 1 and s[i + 1] == "0"):
                next += prev
            # Update the dp variables.
            prev, curr = curr, next
        return curr


def test():
    executors = [
        DP,
        O1DP,
    ]
    tests = [
        ["2101", 1],
        ["0", 0],
        ["1", 1],
        ["12", 2],
        ["82", 1],
        ["27", 1],
        ["226", 3],
        ["06", 0],
        ["106", 1],
        ["206", 1],
        ["123306", 0],
        ["123206", 3],
        ["123123", 9],
        ["1201234", 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numDecodings(t[0])
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
