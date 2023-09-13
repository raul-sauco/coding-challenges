# 135. Candy
# 🔴 Hard
#
# https://leetcode.com/problems/candy/
#
# Tags: Array - Greedy

import timeit
from typing import List


# Use an extra auxiliary vector of the same size as the input vector to
# store the candy assigned to each child initialized to 1 for each child.
# Iterate over the input array forward, for each child that has a higher
# rating that the one to its left, give it one more candy that the one to
# its left already has. Once we reach the end we traverse backwards, for
# each child that has a higher rating than the one to its right, if its it
# not already getting more candy than the one to its right is, we give it
# the amount of candy that that one gets plus 1. We return the sum of
# values in the assigned candy array.
#
# Time complexity: O(n) - We traverse over n elements twice.
# Space complexity: O(n) - We store an extra vector of size n in memory.
#
# Runtime 141 ms Beats 73.84%
# Memory 19.15 MB Beats 91.36%
class TwoArrays:
    def candy(self, ratings):
        n = len(ratings)
        if n < 2:
            return n
        nums = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                nums[i] = nums[i - 1] + 1
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                nums[i - 1] = max(nums[i] + 1, nums[i - 1])
        return sum(nums)


# Similar solution that only uses one pass, keep track of how many
# previous children's assignments depend on the current child, if it is
# necessary to increase its assigned candy, increase it by one for it
# and all previous children that had a higher rating.
#
# Time complexity: O(n) - We visit each of the n elements once and do
# constant time work for each.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 136 ms Beats 88.46%
# Memory 19.26 MB Beats 68.45%
class DescendingSequence:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2:
            return len(ratings)
        # Initialize by giving 1 candy to element 1
        last_rating = ratings[0]
        min_candy = 1
        last_candy = 1
        left_min = 1
        # Keep count of how many descending ratings we have seen in a row
        descending_strike = 1
        for rating in ratings[1:]:
            if rating < last_rating:
                if descending_strike == 1:
                    # It is the first item of the descending sequence
                    # Store the min candy required for the leftmost item
                    left_min = last_candy
                    # Add this item to the current descending sequence count
                descending_strike += 1
                need_to_increment = descending_strike
                if descending_strike <= left_min:
                    # No need to increment the leftmost item of the descending sequence
                    need_to_increment -= 1
                min_candy += need_to_increment
                last_candy = 1

            elif rating == last_rating:
                # There are no requirements if the children have the same rating
                descending_strike = 1
                last_candy = 1
                min_candy += last_candy
            else:
                descending_strike = 1
                last_candy += 1
                min_candy += last_candy

            last_rating = rating
        return min_candy


def test():
    executors = [
        DescendingSequence,
        TwoArrays,
    ]
    tests = [
        [[], 0],
        [[15], 1],
        [[1, 0, 2], 5],
        [[1, 2, 2], 4],
        [[0, 0, 0, 0], 4],
        [[0, 0, 0, -1], 5],
        [[7, 1, 0, -1], 10],
        [[1, 2, 3, 4, 5], 15],
        [[7, 1, 0, -1, -1], 11],
        [[1, 2, 3, 4, 5, 4], 16],
        [[1, 5, 4, 3, 2, 1], 16],
        [[7, 1, 0, -1, -1, 1], 13],
        [[1, 2, 3, 4, 5, 4, 2], 18],
        [[7, 1, 0, -1, -1, 1, 2], 16],
        [[1, 2, 3, 4, 5, 4, 3, 2], 21],
        [[7, 1, 0, -1, -1, 1, 2, 3], 20],
        [[1, 2, 3, 4, 5, 4, 3, 2, 1], 25],
        [[7, 1, 0, -1, -1, 1, 2, 3, 3], 21],
        [[1, 2, 3, 4, 5, 4, 3, 2, 1, 0], 31],
        [[1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0], 32],
        [[1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 1, 2, 4], 41],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.candy(t[0])
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
