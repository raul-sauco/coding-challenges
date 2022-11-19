# Validate Subsequence
# 🟢 Easy
#
# https://www.algoexpert.io/questions/validate-subsequence
#
# Tags: Arrays

import timeit


# Store the index of the first value in the sequence that we haven't yet
# matched, iterate over all the values in array, anytime we find a match
# for the current value in the sequence, we slide the index forward, if
# we match all values we return true, if we get to the end of the input
# array, we return false.
#
# Time complexity: O(n) - Where n is the number of elements in the input
# array.
# Space complexity: O(1) - Constant space.
class Solution:
    def isValidSubsequence(self, array, sequence):
        # The index we are currently trying to match on the
        # sequence.
        i = 0
        for num in array:
            if num == sequence[i]:
                i += 1
                if i == len(sequence):
                    return True
        return False


def test():
    executors = [Solution]
    tests = [
        [[5, 1, 22, 25, 6, -1, 8, 10], [3 - 1, 10], False],
        [[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True],
        [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10], True],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.isValidSubsequence(t[0], t[1])
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
