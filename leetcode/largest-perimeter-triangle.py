# 976. Largest Perimeter Triangle
# 🟢 Easy
#
# https://leetcode.com/problems/largest-perimeter-triangle/
#
# Tags: Array - Math - Greedy - Sorting

import timeit
from collections import deque
from heapq import heapify, heappop
from typing import List


# We need to find the largest values a>b>c such that a<b+c, since that
# is the condition for them to find a triangle.
#
# Time complexity: O(n*log(n)) - The sorting step has the highest cost.
# Space complexity: O(1) - Only the input and output use variable memory.
#
# Runtime: 201 ms, faster than 94.43%
# Memory Usage: 15.5 MB, less than 8.94%
class SortAndGreedy:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            # If the sum of the two shortest sides of the triangle is
            # longer than the longer one, then area > 0, since we start
            # iterating over the bigger sides, this is the largest
            # perimeter.
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


# Similar math to the previous solution but use a heap to get the next
# biggest value, this improves the time complexity on everything except
# the worst case because we will only have to reorder the heap at
# O(log(n)) k times, where k is the number of values we will check.
#
# Time complexity: O(n*log(n)) - The worst case remains the same because
# we pop all elements from the heap at O(log(n)).
# Space complexity: O(1) - Only the input and output use variable memory.
#
# Runtime: 408 ms, faster than 44.4%
# Memory Usage: 15.5 MB, less than 45.85%
class HeapAndGreedy:
    def largestPerimeter(self, nums: List[int]) -> int:
        sides = [-x for x in nums]
        heapify(sides)
        per = deque([])
        while sides:
            per.append(heappop(sides))
            # Append elements to the queue until we have 3, then start
            # checking if this is a valid triangle.
            if len(per) == 3:
                if per[0] > per[1] + per[2]:
                    return -sum(per)
                per.popleft()
        return 0


def test():
    executors = [
        SortAndGreedy,
        HeapAndGreedy,
    ]
    tests = [
        [[1, 2, 1], 0],
        [[2, 1, 2], 5],
        [[3, 6, 2, 3], 8],
        [[2, 1, 2, 1, 1], 5],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.largestPerimeter(t[0])
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
