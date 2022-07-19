# https://leetcode.com/problems/top-k-frequent-elements/

import timeit
from collections import Counter
from typing import List


# Iterate over the elements in nums creating a dictionary with num => num_times_seen
# Return the k most seen elements in the dictionary. For simplicity this solution uses Counter.
#
# Time complexity: O(n*log(n)) - Sorting the dictionary by value.
# Space complexity: O(n) - The size of the dictionary.
#
# Runtime: 163 ms, faster than 48.84% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 18.6 MB, less than 91.62% of Python3 online submissions for Top K Frequent Elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]


def test():
    executors = [Solution]
    tests = [
        [[3, 0, 1, 0], 1, [0]],
        [[1, 1, 1, 2, 2, 2, 2, 3], 3, [2, 1, 3]],
        [[1, 4, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 3], 3, [3, 2, 1]],
        [[1, 1, 1, 2, 2, 3], 2, [1, 2]],
        [[1], 1, [1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.topKFrequent(t[0], t[1])
                exp = t[2]
                assert (
                    result.sort() == exp.sort()
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
