# https://leetcode.com/problems/subarray-sum-equals-k/

# Tags: Array - Hash Table - Prefix Sum

import timeit
from collections import defaultdict
from typing import List


# Create a dictionary to store the prefix sums we have already seen and how many times we have seen each.
# When we calculate each prefix sum we check if the current prefix sum - our target is in the prefix sums
# we have seen. If found, we add its value, the number of times we have seen that prefix sum, to the result
# count. Then we add the prefix sum entry to the dictionary, or add to the previous count if previously seen.
#
# Sum(i,j) = Sum(0,j) - Sum(0,i) => Sum(0,i) = Sum(0,j) - Sum(i,j)
#
# Time complexity: O(n) - we iterate over the elements of the array once and the dictionary once 2*n = O(n)
# checking if the difference is in the dictionary is O(1).
# Space complexity: O(n) - the dictionary will grow to size n.
#
# Runtime: 324 ms, faster than 85.43% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.6 MB, less than 32.25% of Python3 online submissions for Subarray Sum Equals K.
class PrefixSum:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1

        # Calculate all prefix sums
        res, sum = 0, 0
        for num in nums:
            # Calculate the prefix sum at this element
            sum += num

            # If we can get k with this element and one, or multiple, previous ones, add that to the result set
            if sum - k in sums:
                res += sums[sum - k]

            # Add this prefix sum to the sums dictionary
            sums[sum] += 1

        return res


def test():
    executors = [PrefixSum]
    tests = [
        [[1, 1, 1], 2, 2],
        [[1, 2, 3], 3, 2],
        [[1], 0, 0],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.subarraySum(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
