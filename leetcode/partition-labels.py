# 763. Partition Labels
# 🟠 Medium
#
# https://leetcode.com/problems/partition-labels/
#
# Tags: Hash Table - Two Pointers - String - Greedy

import timeit
from typing import List


# Iterate over the characters in O(n) to find the smallest intervals
# that contain each character, then iterate over the intervals merging
# them and recording their length to return as an array.
#
# Time complexity: O(n) - We iterate once over all the characters in the
# input s and then once over the intervals, the number of which equals
# the number of unique characters in the string, max 26.
# Space complexity: O(1) - The dictionary of char: interval has a max
# size of 26, the second loop uses constant space.
#
# Runtime: 60 ms, faster than 69.20%
# Memory Usage: 13.8 MB, less than 68.63%
class Intervals:
    def partitionLabels(self, s: str) -> List[int]:
        # First section, find intervals for each character.
        intervals = {}
        for i, char in enumerate(s):
            if char not in intervals:
                intervals[char] = [i, i]
            else:
                intervals[char][1] = i
        # Second section, merge intervals, we only need to preserve one.
        res = []
        last_interval = None
        # Iterate over the intervals found.
        for interval in intervals.values():
            if not last_interval:
                last_interval = interval
                continue
            # If there is overlap, merge them.
            if interval[0] < last_interval[1]:
                last_interval[1] = max(last_interval[1], interval[1])
            # If there is no overlap, add the length of the last
            # interval to the result and the current interval becomes
            # the last interval.
            else:
                res.append(last_interval[1] - last_interval[0] + 1)
                last_interval = interval
        # After the loop there will be one interval left unprocessed.
        res.append(last_interval[1] - last_interval[0] + 1)
        return res


# TODO add the greedy solution that uses a pointer to the last char pos.


def test():
    executors = [
        Intervals,
    ]
    tests = [
        ["a", [1]],
        ["ab", [1, 1]],
        ["eccbbbbdec", [10]],
        ["abcbdde", [1, 3, 2, 1]],
        ["abcde", [1, 1, 1, 1, 1]],
        ["ababcbacadefegdehijhklij", [9, 7, 8]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.partitionLabels(t[0])
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
