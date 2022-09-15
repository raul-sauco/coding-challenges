# 2007. Find Original Array From Doubled Array
# 🟠 Medium
#
# https://leetcode.com/problems/find-original-array-from-doubled-array/
#
# Tags: Array - Hash Table - Greedy - Sorting

import timeit
from collections import Counter
from typing import List


# Use a Counter to find element doubles in O(1), iterate over the input
# in O(n) checking if we have used them already, they were some other
# element's double, or if they have a double.
#
# Time complexity: O(n*log(n)) - The sorting step has the highest cost.
# Space complexity: O(n) - The counter and the result.
#
# Runtime: 3863 ms, faster than 5.13%
# Memory Usage: 32.2 MB, less than 70.28%
class SortAndCounter:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # If the array is of uneven length, it cannot be a doubled array.
        if len(changed) % 2 != 0:
            return []
        # Array to store original elements. We could initialize it to
        # half the size of changed, then use a pointer to see where to
        # insert, but amortized O(1) insertion is still better than
        # tho O(n*log(n)) from the sorting.
        res = []
        # Count the element frequency in O(n).
        c = Counter(changed)
        # Iterate O(n) over the sorted O(n*log(n)) elements.
        for val in sorted(changed):
            # If we have used up all occurrences of this number, move
            # to the next.
            if not val in c:
                continue
            # Val is in c, check if val * 2 also is available.
            double = val * 2
            # If double is in c, val was one of the original values.
            if double in c:
                res.append(val)
                c[val] -= 1
                if not c[val]:
                    del c[val]
                c[double] -= 1
                if not c[double]:
                    del c[double]
        # There are several ways to check if the array is doubled after
        # processing all the values, for example, the length of res has
        # to be exactly half of the length of changed, but we can also
        # check that we have used up all elements.
        if c:
            return []
        # If we have used up all the elements, return the result.
        return res


# The previous solution does unnecessary work when we have many repeated
# values in the array, we can optimize if we sort the counter and check
# validity against the counts instead of iterating over the repeated
# values one by one.
#
# Time complexity: O(n+k*log(k)) - Where n is the number of values in
# the input and k is the number of unique values in the input.
# Space complexity: O(k) - The counter can only grow to size k. If we
# take into account the result array, it would be O(n). k could be == n.
#
# Runtime: 2430 ms, faster than 41.29%
# Memory Usage: 32.6 MB, less than 55.78%
class SortCounter:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # If the length is uneven, it cannot be a changed array.
        if len(changed) % 2 != 0:
            return []
        c = Counter(changed)
        for key in sorted(c):
            double = key * 2
            # If we don't have enough doubles for each occurrence of
            # key, this cannot be a doubled array.
            if c[key] > c[double]:
                return []
            # Update the count of double taking care of the special case
            # when the key is zero.
            c[double] -= c[key] if key else c[double] // 2
        # If all the values are, or have, a double, the array is doubled.
        return [val for val in c.elements()]


def test():
    executors = [
        SortAndCounter,
        SortCounter,
    ]
    tests = [
        [[], []],
        [[6, 3, 0, 1], []],
        [[0, 0, 0, 0], [0, 0]],
        [[1, 3, 4, 2, 6, 8], [1, 3, 4]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findOriginalArray(t[0])
                exp = t[1]
                # Sort the result because it can be in any order.
                result.sort()
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
