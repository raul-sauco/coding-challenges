# https://leetcode.com/problems/longest-consecutive-sequence/

import timeit
from typing import List


class Sequence:
    def __init__(self, val: int):
        self.length = 1
        self.start = val
        self.end = val

    def prepend(self, val: int) -> int:
        if val != self.start - 1:
            raise Exception(f'{val} does not precede {self.start}')
        self.start = val
        self.length += 1
        return self.length

    def append(self, val: int) -> int:
        if val != self.end + 1:
            raise Exception(f'{val} does not follow {self.start}')
        self.end = val
        self.length += 1
        return self.length

    # seq is Sequence and seen a dictionary {int: Sequence}
    def mergeAppend(self, seq, seen) -> int:
        if self.end + 2 != seq.start:
            raise Exception(
                f'Sequences cannot be merged. end:start {self.end}:{seq.start}')
        self.end = seq.end
        self.length += seq.length + 1
        # Update all the pointers in seen to point to this sequence
        for num in range(seq.start, seq.end + 1):
            seen[num] = self
        return self.length


# Runtime: 833 ms, faster than 42.65% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 37.1 MB, less than 6.04 % of Python3 online submissions for Longest Consecutive Sequence.
class HashSet:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Keep a dictionary of numbers seen and the sequences they are assigned to
        seen = {}
        max_length = 0
        for n in nums:
            if n in seen:
                continue
            else:
                # Check if we can append to any sequence
                if n-1 in seen:
                    # If we can append and prepend, merge the sequences
                    if n+1 in seen:
                        sequence_length = seen[n -
                                               1].mergeAppend(seen[n+1], seen)
                    else:
                        # Otherwise just append
                        sequence_length = seen[n-1].append(n)
                    seen[n] = seen[n-1]
                elif n+1 in seen:
                    # We cannot append but can prepend to a sequence
                    sequence_length = seen[n+1].prepend(n)
                    seen[n] = seen[n+1]
                else:
                    # We cannot append or prepend, create a new sequence
                    seen[n] = Sequence(n)
                    sequence_length = 1

                # Update the maximum length seen
                if sequence_length > max_length:
                    max_length = sequence_length

        return max_length

# This solution is slow for complete decreasing sets
# [100, 99, 98, 97...]
# Because the inner loop will run through the whole sequence for each element.


class Set:
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best

# Sorting has a O(n*log(n)) complexity


class Sorting:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums.sort()

        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1

        return max(longest_streak, current_streak)


def test():
    executors = [
        {'executor': HashSet, 'title': 'HashSet', },
        {'executor': Set, 'title': 'Set', },
        {'executor': Sorting, 'title': 'Sorting', },
    ]
    tests = [
        [[100, 4, 200, 1, 3, 2], 4],
        [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9],
        [[x for x in range(1000000, -10000000, -1)], 11000000],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = executor['executor']()
                result = sol.longestConsecutive(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(
            executor['title'], used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
