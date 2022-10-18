# 38. Count and Say
# 🟠 Medium
#
# https://leetcode.com/problems/count-and-say/
#
# Tags: String

import timeit
from typing import List

# 1e3 calls with input 30.
# » HelperFn            1.83325   seconds
# » Recursive           1.88734   seconds

# Define a helper function to "say" the numbers iterating over the input
# digits and creating groups, then using the group length and content to
# generate the result.
#
# Time complexity: O(n*m) - n is the input and m is the average length of
# of the string generated. Since the input is fixed at 30, we could call
# it O(1) because the max length of both n and m is known.
# Space complexity: O(m) - m is the longest strings generated that needs
# to be stored in memory.
#
# Runtime: 115 ms, faster than 16.46%
# Memory Usage: 14.5 MB, less than 7.99%
class HelperFn:
    def countAndSay(self, n: int) -> str:
        # Not necessary to handle base case but easier to read.
        if n == 1:
            return "1"
        # Define a function that "says" the last number.
        def sayNum(digits: List[str]) -> List[str]:
            # Store the new result.
            spelled = []
            group = []
            for digit in digits:
                if not group:
                    group.append(digit)
                    continue
                if digit == group[-1]:
                    group.append(digit)
                else:
                    # Append the last group to the result.
                    spelled.append(str(len(group)))
                    spelled.append(group[-1])
                    # Start a new group.
                    group = [digit]
            # Append the last group.
            spelled.append(str(len(group)))
            spelled.append(group[-1])
            return spelled

        # Store the numbers we generate
        last = ["1"]
        # Iterate over the input counting the number of repeated digits.
        for _ in range(2, n + 1):
            last = sayNum(last)
        return "".join(last)


# Use the recursive nature of the problem to call the countAndSay
# function recursively to generate the previous number. This has the
# disadvantage that we need to join the string lists into strings at
# every step but it seems to perform better in the tests.
#
# Time complexity: O(n*m) - n is the input and m is the average length of
# of the string generated. Since the input is fixed at 30, we could call
# it O(1) because the max length of both n and m is known.
# Space complexity: O(n*m) - The depth of the call stack times the
# length of the intermediate results.
#
# Runtime: 93 ms, faster than 41.88%
# Memory Usage: 14.1 MB, less than 16.06%
class Recursive:
    def countAndSay(self, n: int) -> str:
        # Base case.
        if n == 1:
            return "1"
        # Obtain the value we need to "say".
        prev = self.countAndSay(n - 1)

        # Store the new result.
        spelled = []
        group = []
        for digit in prev:
            if not group:
                group.append(digit)
                continue
            if digit == group[-1]:
                group.append(digit)
            else:
                # Append the last group to the result.
                spelled.append(str(len(group)))
                spelled.append(group[-1])
                # Start a new group.
                group = [digit]

        # Append the last group.
        spelled.append(str(len(group)))
        spelled.append(group[-1])
        return "".join(spelled)


def test():
    executors = [
        HelperFn,
        Recursive,
    ]
    tests = [
        [1, "1"],
        [4, "1211"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countAndSay(t[0])
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
