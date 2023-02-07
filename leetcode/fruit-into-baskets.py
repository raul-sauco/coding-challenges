# 904. Fruit Into Baskets
# 🟠 Medium
#
# https://leetcode.com/problems/fruit-into-baskets/
#
# Tags: Array - Hash Table - Sliding Window

import timeit
from collections import defaultdict
from typing import List


# Iterate over the array keeping count of the length of the last groups
# of similar fruit trees, once we decide to start picking fruit, we
# cannot stop, the only decision we need to make is where to start.
#
# Time complexity: O(n) - We visit each element once and do O(1) work.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 879 ms Beats 86.42%
# Memory 20.4 MB Beats 28.87%
class Greedy:
    def totalFruit(self, fruits: List[int]) -> int:
        # Base case, less than 3 trees.
        if len(fruits) < 3:
            return len(fruits)
        # The most fruit we can pick.
        res = 0
        # The start index of the last sequence.
        last_idx = 0
        # The length and type of the previous sequence.
        prev = (0, -1)
        # The length of the current sequence that we are processing.
        cur = 1
        for i in range(1, len(fruits)):
            # If we find the same type as the previous tree.
            if fruits[i] == fruits[i - 1]:
                cur += 1
            # If we find a different type from the previous tree we have
            # to handle two different cases, the tree is the same as the
            # previous tree that we were collecting or it isn't.
            elif fruits[i] == prev[1]:
                # In this case, one of the baskets has this tree, we
                # can switch baskets and keep collecting.
                prev, cur = (cur, fruits[i - 1]), prev[0] + 1
                last_idx = i
            else:
                # But, if the current tree is different to both trees
                # that we were collecting, we need to start collecting
                # this new tree, and we could have collected the
                # previous tree up to the last point it changed.
                prev = (i - last_idx, fruits[i - 1])
                cur = 1
                last_idx = i
            res = max(res, prev[0] + cur)
        return max(res, prev[0] + cur)


# The sliding window solution has the same complexity as the previous
# solution but it is easier to understand and implement.
#
# Time complexity: O(n) - We visit each element once and do O(1) work.
# Space complexity: O(1) - We use constant extra memory, two pointers
# and a hashmap of max size == 3.
#
# Runtime 1006 ms Beats 62.8%
# Memory 20.5 MB Beats 13.87%
class SlidingWindow:
    def totalFruit(self, fruits: List[int]) -> int:
        # A hashmap of the fruits inside the current sliding window.
        cur = defaultdict(int)
        # The left pointer and the length of the longest window.
        l, res = 0, 0
        for r, f in enumerate(fruits):
            cur[f] += 1
            # We can have at most 2 types of fruit inside the sliding
            # window.
            while len(cur) > 2:
                # Pop the leftmost element.
                cur[fruits[l]] -= 1
                if cur[fruits[l]] == 0:
                    cur.pop(fruits[l])
                l += 1
            # We have at most 2 types of fruit inside the window.
            res = max(res, r - l + 1)
        return res


def test():
    executors = [
        Greedy,
        SlidingWindow,
    ]
    tests = [
        [[], 0],
        [[1], 1],
        [[1, 2], 2],
        [[1, 2, 3], 2],
        [[1, 2, 1], 3],
        [[0, 1, 2, 2], 3],
        [[1, 2, 3, 2, 2], 4],
        [[1, 2, 2, 3, 2, 2, 2, 3, 3, 4, 3], 8],
        [[1, 2, 2, 3, 2, 1, 2, 3, 3, 4, 3, 4, 3, 4, 3], 8],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.totalFruit(t[0])
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
