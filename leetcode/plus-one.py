# https://leetcode.com/problems/plus-one/

# Tags: Array - Math

import timeit
from typing import List

# One approach would be to convert the list to an integer, then add 1, then convert to list again but that would be
# less performant, for the average case, than adding one to the last digit and taking care of the carry.

# Start adding from the last digit, treat 9 as a special case because of the carry operation.
#
# Time complexity: O(log(n)) - in the worst case when the sum carries all the way. O(1) best case.
# Space complexity: O(1) - Fixed size set to store the replacements
#
# Runtime: 29 ms, faster than 97.76% of Python3 online submissions for Plus One.
# Memory Usage: 13.8 MB, less than 58.40% of Python3 online submissions for Plus One.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        replacements = {
            9: 0,
            8: 9,
            7: 8,
            6: 7,
            5: 6,
            4: 5,
            3: 4,
            2: 3,
            1: 2,
            0: 1,
        }
        idx = -1
        while True:
            if digits[idx] == 9:
                digits[idx] = 0
                if idx == -len(digits):
                    # If we are on the leftmost digit and it is a 9, replace it with 0 and prepend a 1
                    digits = [1] + digits
                    return digits
                else:
                    idx -= 1
            else:
                # Add one to the current digit and we are done
                digits[idx] = replacements[digits[idx]]
                return digits


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3], [1, 2, 4]],
        [[4, 3, 2, 1], [4, 3, 2, 2]],
        [[9], [1, 0]],
        [[1, 9, 9, 9, 9], [2, 0, 0, 0, 0]],
        [[9, 9, 9, 9], [1, 0, 0, 0, 0]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                result = sol.plusOne(t[0])
                exp = t[1]
                assert result == exp, f"\033[93m» {t[0]} <> {exp}\033[91m for test {i} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
