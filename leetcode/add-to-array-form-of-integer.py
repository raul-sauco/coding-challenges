# 989. Add to Array-Form of Integer
# 🟢 Easy
#
# https://leetcode.com/problems/add-to-array-form-of-integer/
#
# Tags: Array - Math

import timeit
from typing import List


# We can use a new array to build the result, iterate over the digits
# in num and use a separate value for a carry, for each digit, we will
# compute the sum of digit, k and carry.
#
# Time complexity: O(max(n, log(k))) - On each loop we consume one digit
# of num and divide k by 10, the loops will keep going as long as we
# have digits or k is not zero.
# Space complexity: O(max(n, log(k))) - The number of digits in the
# result is directly proportional to the longest between the number of
# digits in num and k.
#
# Runtime 292 ms Beats 86.73%
# Memory 15.2 MB Beats 11.71%
class ResultArray:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res, carry, op, nums = [], 0, k, num[::]
        # Iterate over the digits in nums.
        while nums or carry or op:
            d = nums.pop() if nums else 0
            # The current digit will be the sum of the digit of nums,
            # the current carry and the matching digit of k.
            cur = d + carry + op % 10
            # Discard the current last digit of k.
            op //= 10
            res.append(cur % 10)
            carry = cur // 10
        return list(reversed(res))


# If we are allowed to mutate the input array, we can use it to compute
# the result by using k directly as the carry, we iterate over the
# digits in num from right to left adding the current carry, we use mod
# to compute the resulting digit and div // 10 to "consume" the current
# carry digit.
#
# Time complexity: O(max(n, log(k))) - On each loop we consume one digit
# of num and divide k by 10, the loops will keep going as long as we
# have digits or k is not zero.
# Space complexity: O(max(n, log(k))) - The number of digits in the
# result is directly proportional to the longest between the number of
# digits in num and k.
#
# Runtime 272 ms Beats 95.10%
# Memory 14.8 MB Beats 98.4%
class UpdateInput:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in reversed(range(len(num))):
            k += num[i]
            num[i] = k % 10
            k //= 10
        return [int(x) for x in str(k)] + num if k else num


def test():
    executors = [
        ResultArray,
        UpdateInput,
    ]
    tests = [
        [[2, 7, 4], 181, [4, 5, 5]],
        [[9], 9999, [1, 0, 0, 0, 8]],
        [[2, 1, 5], 806, [1, 0, 2, 1]],
        [[1, 2, 0, 0], 34, [1, 2, 3, 4]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.addToArrayForm(t[0], t[1])
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
