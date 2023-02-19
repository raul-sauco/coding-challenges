# 926. Flip String to Monotone Increasing
# 🟠 Medium
#
# https://leetcode.com/problems/flip-string-to-monotone-increasing/
#
# Tags: String - Dynamic Programming

import timeit


# Do one pass forward counting the number of updates we would need to
# do if the switch point between 0s and 1s was at the last index, i.e.
# if we converted the entire string to 0s. Then start iterating back,
# checking how many updates we would need to have the inflection point
# at the current index, if we see a 1, we can subtract one from the
# current count of updates, we would not have needed to update that
# position to be a 1, if we see a 0, we would have needed one more
# update for that position to be a 1.
#
# Time complexity: O(n) - We traverse the string twice, once forward and
# once in reverse.
# Space complexity: O(1) - We use two integers and an iterator of extra
# memory.
#
# Runtime 122 ms Beats 94.87%
# Memory 14.8 MB Beats 96.47%
class Windows:
    def minFlipsMonoIncr(self, s: str) -> int:
        updates = 0
        # One pass forward counting the number of ones we would need to
        # convert to zeroes to have an increasing, all zeroed string.
        for c in s:
            if c == "1":
                updates += 1
        # This is the best result right now.
        res = updates
        # Iterate back computing the number of updates to have the
        # string be increasing with the switch point at that index.
        for c in reversed(s):
            # If we see a 0, we would have need to update this character
            # to be a 1.
            if c == "0":
                updates += 1
            # If we see a 1, this is one update we would not have needed.
            else:
                updates -= 1
                if updates < res:
                    res = updates
        return res


# Use dynamic programming, count the number of changes to make each
# prefix monotonically increasing given the result of the prefix one
# character shorter.
#
# Time complexity: O(n) - We visit each value once.
# Space complexity: O(1) - We store two integers.
#
# Runtime 89 ms Beats 99.68%
# Memory 14.8 MB Beats 93.27%
class DP:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = res = 0
        for c in s:
            if c == "1":
                # We can append a 1 to the right at no extra cost.
                ones += 1
            else:
                # We need to decide whether it is better to flip this 0
                # to a 1 or would have been better to flip all 1s in the
                # prefix to a 0.
                # res = min(ones, res + 1)
                res += 1
                if ones < res:
                    res = ones
        return res


def test():
    executors = [
        Windows,
        DP,
    ]
    tests = [
        ["0", 0],
        ["1", 0],
        ["0011", 0],
        ["00110", 1],
        ["010110", 2],
        ["00011000", 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.minFlipsMonoIncr(t[0])
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
