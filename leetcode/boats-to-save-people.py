# 881. Boats to Save People
# 🟠 Medium
#
# https://leetcode.com/problems/boats-to-save-people/
#
# Tags: Array - Two Pointers - Greedy - Sorting

import timeit
from typing import List


# Sort the weights of the people that we need to save, then use two
# pointers, one for the heaviest person that needs to be saved and one
# for the lightest, if we can put them together on a boat, do so and
# shift both pointers, otherwise put the heaviest person alone in a boat
# and move only that pointer. This works because if the heaviest person
# cannot go on the boat together with the current lightest person, we
# know that it cannot also go with any other.
#
# Time complexity: O(n*log(n)) - Sorting has the most complexity, then
# arranging people on boats we can do in O(n).
# Space complexity: O(n) - Sorting takes memory in Python.
#
# Runtime 453 ms Beats 84.42%
# Memory 20.9 MB Beats 60.46%
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0
        while l <= r:
            # Consume one boat.
            res += 1
            # If we can fit both people on this boat, do it and move to
            # the next likely pair.
            if people[l] + people[r] <= limit:
                l += 1
            # The heavy person always goes in the boat.
            r -= 1
        return res


def test():
    executors = [Solution]
    tests = [
        [[1, 2], 3, 1],
        [[3, 2, 2, 1], 3, 3],
        [[3, 5, 3, 4], 5, 4],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.numRescueBoats(t[0], t[1])
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
