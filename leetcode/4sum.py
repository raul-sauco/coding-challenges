# 18. 4Sum
# 🟠 Medium
#
# https://leetcode.com/problems/4sum/
#
# Tags: Array - Two Pointers - Sorting

import json
import os
import timeit
from collections import Counter, defaultdict
from typing import List


# Similar to two sum but create entries for each sum of pairs of
# elements in O(n^2) time and space, and use these sums to find matching
# quadruplets, when found, we can add them to the result set as a sorted
# tuple to eliminate duplicates.
#
# Time complexity: O(n^3) - First we iterate three times over the input
# to eliminate any elements that appear more than four times, then we
# iterate over each pair of elements computing their sum and checking
# to see if their complementary sum has been seen already, if the
# complementary is found, it points to a list of pairs that sum up to
# that complementary, that list could be of length n although the
# probability is low, that is three levels of nesting n calls at worst.
# Space complexity: O(n^2) - The sums dictionary could have an entry for
# each pair of elements in the input.
#
# Runtime 138 ms Beats 86.55%
# Memory 18.3 MB Beats 5.4%
class HMSol:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Leave at most 4 of each.
        freq = Counter(nums)
        for k, v in freq.items():
            if v > 4:
                freq[k] = 4
        nums = list(freq.elements())
        # Use a hashmap of pair sums to the values that make the sum.
        seen, n, res = defaultdict(list), len(nums), set()
        # Iterate over every pair of indexes.
        for i in range(n - 1):
            for j in range(i + 1, n):
                pair_sum = nums[i] + nums[j]
                complement = target - pair_sum
                if complement in seen:
                    for pair in seen[complement]:
                        if i not in pair and j not in pair:
                            res.add(
                                tuple(
                                    sorted(
                                        [
                                            nums[pair[0]],
                                            nums[pair[1]],
                                            nums[i],
                                            nums[j],
                                        ]
                                    )
                                )
                            )
                seen[pair_sum].append((i, j))
        return res


# Runtime 634 ms Beats 77.76%
# Memory 13.9 MB Beats 53.75%
class TwoPointerSol:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sorting the numbers lets us skip the same value in the same
        # position later.
        vals = sorted(nums)
        # Removing k-plicates does not improve the performance.
        # k = 4
        # w = r = 0
        # while r < len(vals):
        #     vals[w] = vals[r]
        #     if not (r > k and vals[r] == vals[r - k]):
        #         w += 1
        #     r += 1
        # vals = vals[:w]
        res, current = [], []
        # Define an internal function that picks the next number.
        def kSum(k, start, t):
            # This should actually never happen.
            # if k <= 2:
            #     raise Exception("K should not be <= 2!")
            # Pick the next digit and call the next level.
            for i in range(start, len(vals) + 1 - k):
                # Avoid picking the same value in the same position.
                if i > start and vals[i] == vals[i - 1]:
                    continue
                current.append(vals[i])
                if k == 3:
                    twoSum(i + 1, t - vals[i])
                else:
                    kSum(k - 1, i + 1, t - vals[i])
                # Now backtrack.
                current.pop()

        # Define an internal function that picks two values that add up
        # to a given target in a sorted array suffix if they exists.
        def twoSum(start, t):
            l, r = start, len(vals) - 1
            while l < r:
                s = vals[l] + vals[r]
                if s < t:
                    l += 1
                elif t < s:
                    r -= 1
                # Otherwise we found a match.
                else:
                    res.append(current + [vals[l], vals[r]])
                    # Still trying to find more matches.
                    l += 1
                    while l < r and vals[l] == vals[l - 1]:
                        l += 1

        # Initial call
        kSum(4, 0, target)
        return res


def test():
    executors = [
        HMSol,
        TwoPointerSol,
    ]
    # The tests are big, use a separate JSON file.
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(os.path.join(__location__, "4sum.json")) as json_file:
        tests = json.load(json_file)
        for executor in executors:
            start = timeit.default_timer()
            for _ in range(1):
                for col, t in enumerate(tests):
                    sol = executor()
                    result = sol.fourSum(t[0], t[1])
                    # The OJ accepts the elements in any order.
                    result = set([tuple(sorted(x)) for x in result])
                    exp = set(map(tuple, t[2]))
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
