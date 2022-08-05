# 40. Combination Sum II
# 🟠 Medium
#
# https://leetcode.com/problems/combination-sum-ii/
#
# Tags: Array - Backtracking

import timeit
from collections import Counter
from typing import List


# We can find out the frequency of each unique value in the candidates
# array. For each value, we find the range
# [0..min(target // value, value_frequency)]
# And for each of the possible choices, we explore each branch that it
# would generate.
#
# Time complexity: O(2^t) - At each level of the decision tree, we can
# choose to use or not every value and the decision tree can have height
# t, for example if one of the solutions is all 1s.
# Space complexity: O(2^t) - The call stack, same reasoning as the time
# complexity.
#
# Runtime: 96 ms, faster than 67.30%
# Memory Usage: 14.2 MB, less than 5.59%
class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        # Store the results in a list.
        results = []
        # Remove all candidates greater than the target.
        frequencies = Counter([num for num in candidates if num <= target])
        # Define a function that takes a dictionary of value frequencies
        # and a current target integer.
        def dfs(res: List[int], freq: Counter, ct: int) -> None:
            # num = freq.most_common(1)[0][0]
            num = next(iter(freq))
            # Take 0..n times the first value in freq
            r = min(ct // num, freq[num]) + 1
            for n in range(r):
                # Compute the value of adding this number n times to the
                # result.
                val = num * n
                if val == ct:
                    # If adding this value to the result n number of
                    # times adds up to the target, add that to the
                    # result set. The solution expects sorted lists.
                    results.append(sorted(res + ([num] * n)))
                elif val < ct:
                    # If adding this value this number of times still
                    # falls short of the target, make a copy of the
                    # dictionary to pass to the recursive call.
                    freq_copy = freq.copy()
                    freq_copy[num] -= 1
                    # We already considered this entry n times, we don't
                    # want to consider it on the sub-calls, instead the
                    # for loop takes care of iterating over the possible
                    # number of occurrences.
                    del freq_copy[num]
                    # If we still have any values to add in frequencies.
                    if freq_copy:
                        dfs(res + ([num] * n), freq_copy, ct - val)

        # Initial call, don't bother if none of the values can be used.
        if frequencies:
            # Converting the counter to a dictionary before all the
            # copying it speeds up the
            dfs([], dict(frequencies), target)
        return results


def test():
    executors = [Solution]
    tests = [
        [[10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]],
        [[2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]],
        [[2], 1, []],
        [[2], 2, [[2]]],
        [[2, 3, 6, 7, 2], 7, [[2, 2, 3], [7]]],
        [[7, 3, 6, 2], 7, [[7]]],
        [[2, 3, 5], 8, [[3, 5]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.combinationSum2(t[0], t[1])
                result.sort()
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
