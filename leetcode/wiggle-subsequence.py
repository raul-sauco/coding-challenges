# https://leetcode.com/problems/wiggle-subsequence/

import timeit
from typing import List
from matplotlib import pyplot as plt


# Runtime: 55 ms, faster than 53.05% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 14 MB, less than 36.01 % of Python3 online submissions for Wiggle Subsequence.
class LinearDP:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)


# Runtime: 67 ms, faster than 34.51% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 13.9 MB, less than 77.55 % of Python3 online submissions for Wiggle Subsequence.
class Greedy:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prev_diff = nums[1] - nums[0]
        count = 2 if prev_diff != 0 else 1
        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff
        return count


class GreedyFlag:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 1
        result = []
        up = None  # current is increasing or not
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up != True:
                result.append(nums[i-1])
                length += 1
                up = True
            if nums[i] < nums[i - 1] and up != False:
                result.append(nums[i-1])
                length += 1
                up = False
        return length


def test():
    executor = [
        {'executor': LinearDP, 'title': 'LinearDP', },
        {'executor': Greedy, 'title': 'Greedy', },
        {'executor': GreedyFlag, 'title': 'GreedyFlag', },
    ]
    tests = [
        [[1, 7, 4, 9, 2, 5], 6],
        [[1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7],
        [[22, 17, 5, 10, 13, 15, 10, 5, 16, 8], 6],
        [[1, 2, 3, 4, 5, 6, 7, 8, 9], 2],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = e['executor']()
                result = sol.wiggleMaxLength(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()


def plot():
    values = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    for x, y in enumerate(values):
        plt.bar(x, y)
    plt.show()


# plot()
