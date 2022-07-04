# https://leetcode.com/problems/candy/


import timeit
from typing import List


# Runtime: 263 ms, faster than 42.85% of Python3 online submissions for Candy.
# Memory Usage: 16.9 MB, less than 37.74 % of Python3 online submissions for Candy.
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


class TwoArrays:
    def candy(self, ratings):
        n = len(ratings)
        if n < 2:
            return n

        # initial state: each kid gets one candy
        nums = [1] * n
        # kids on upwards curve get candies
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1

        # kids on downwards curve get candies
        # if a kid on both up/down curves, i.e. a peak or a valley
        # kid gets the maximum candies among the two.
        # total = 0
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                nums[i-1] = max(nums[i]+1, nums[i-1])
            # total += nums[i]

        # Locally it is quicker to return the sum
        # total += nums[0]
        # return total
        return sum(nums)


def test():
    executor = [
        {'executor': DescendingSequence, 'title': 'DescendingSequence', },
        {'executor': TwoArrays, 'title': 'TwoArrays', },
    ]
    tests = [
        [[0, 0, 0, 0], 4],
        [[0, 0, 0, -1], 5],
        [[7, 1, 0, -1], 10],
        [[7, 1, 0, -1, -1], 11],
        [[7, 1, 0, -1, -1, 1], 13],
        [[7, 1, 0, -1, -1, 1, 2], 16],
        [[7, 1, 0, -1, -1, 1, 2, 3], 20],
        [[7, 1, 0, -1, -1, 1, 2, 3, 3], 21],
        [[1, 2, 3, 4, 5], 15],
        [[1, 2, 3, 4, 5, 4], 16],
        [[1, 2, 3, 4, 5, 4, 2], 18],
        [[1, 2, 3, 4, 5, 4, 3, 2], 21],
        [[1, 2, 3, 4, 5, 4, 3, 2, 1], 25],
        [[1, 2, 3, 4, 5, 4, 3, 2, 1, 0], 31],
        [[1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0], 32],
        [[1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 1, 2, 4], 41],
        [[1, 5, 4, 3, 2, 1], 16],
        [[1, 0, 2], 5],
        [[1, 2, 2], 4],
        [[], 0],
        [[15], 1],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = e['executor']()
                result = sol.candy(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
