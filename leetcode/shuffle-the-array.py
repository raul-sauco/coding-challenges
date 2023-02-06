# 1470. Shuffle the Array
# 🟢 Easy
#
# https://leetcode.com/problems/shuffle-the-array/
#
# Tags: Array

import timeit
from typing import List


# Iterate over n positions adding elements to the result, for each
# value of n, we add the element at the corresponding index idx and the
# element at n + idx.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - If we don't take into account the input and
# output arrays.
#
# Runtime 61 ms Beats 79.49%
# Memory 14.1 MB Beats 86.30%
class Naive:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [el for i in range(n) for el in (nums[i], nums[n + i])]
        # res = []
        # for i in range(n):
        #     res.append(nums[i])
        #     res.append(nums[n + i])
        # return res


# This solution covers the hypothetical case that we were asked to solve
# the problem without using any extra memory, only the input string. We
# use the fact that the values on the input array are guaranteed to be
# less or equal to 10^3, which means that they will only use a maximum
# of 10 bits, and fit two values together in each element, then we
# unpack the values into the corresponding indexes and return the result.
#
# Time complexity: O(n) - We iterate twice over the input array.
# Space complexity: O(1) - We don't use any extra memory.
#
# Runtime 66 ms Beats 53.96%
# Memory 14.1 MB Beats 86.25%
class BitManipulation:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] |= nums[n + i] << 10
        # Place the values in their corresponding indexes.
        for i in reversed(range(n)):
            # The order is important, otherwise nums[1] is updated after
            # nums[0] resulting in a wrong value.
            nums[2 * i + 1] = nums[i] >> 10
            nums[2 * i] = nums[i] & 1023
        return nums


def test():
    executors = [
        Naive,
        BitManipulation,
    ]
    tests = [
        [[1, 1, 2, 2], 2, [1, 2, 1, 2]],
        [[2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]],
        [[1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.shuffle(t[0], t[1])
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
