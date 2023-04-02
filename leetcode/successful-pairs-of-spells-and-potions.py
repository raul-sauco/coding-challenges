# 2300. Successful Pairs of Spells and Potions
# 🟠 Medium
#
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
#
# Tags: Array - Two Pointers - Binary Search - Sorting

import json
import os
import timeit
from bisect import bisect_left
from math import ceil
from typing import List


# Use the built-in bisect function, since we want to guarantee that
# spell * potion >= success, which is equivalent to potion >=
# ceil(success / spell) we can use bisect_left to find the position at
# which we would insert potion.
#
# Time complexity: O(n*log(n)+m*log(n)) - Where m is the number of spells
# and n is the number of potions. We sort the potions array at nlog(n)
# cost, then iterate over the spells, for each spell, we binary search
# the number of potions that can be combined with the spell to result in
# a successful combination.
# Space complexity: O(m+n) - Sorting the potions array of n positions
# can take up to n/2, the result array has size m.
#
# Runtime 1177 ms Beats 99.15%
# Memory 37 MB Beats 69.69%
class BuiltInBisect:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        return [
            len(potions) - bisect_left(potions, ceil(success / spell))
            for spell in spells
        ]


# Sort the potions array, then iterate over the spells, for each spell,
# find the index of the first potion that we can combine with it to
# satisfy the success value.
#
# Time complexity: O(n*log(n)+m*log(n)) - Where m is the number of spells
# and n is the number of potions. We sort the potions array at nlog(n)
# cost, then iterate over the spells, for each spell, we binary search
# the number of potions that can be combined with the spell to result in
# a successful combination.
# Space complexity: O(m+n) - We make a copy of the potions array n and
# sort it, the result array has size m.
#
# Runtime 1945 ms Beats 42.49%
# Memory 37.3 MB Beats 33.99%
class BinarySearchPotions:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        # Sort the potions to binary search.
        potions.sort()
        n = len(potions)
        res = [0] * len(spells)
        for i, spell_force in enumerate(spells):
            # Left pointer points to the right-most known non-successful
            # potion, right points to the left-most known
            # successful potion,
            l, r = -1, n
            while l < r - 1:
                mid = (l + r) // 2
                combined_force = spell_force * potions[mid]
                if combined_force < success:
                    l = mid
                else:
                    r = mid
            res[i] = n - r
        return res


# Similar to the previous binary search solution but it also sorts the
# spells, then, once we find the number of potions useful with one
# spell, we know that we can use that as the right boundary for the
# next spell because its value is greater.
#
# Time complexity: O(n*log(n)+m*log(n)+m*log(m)) - Where m is the number
# of spells and n is the number of potions. We sort the potions array at
# nlog(n) cost, then iterate over the spells, for each spell, we binary
# search the number of potions that can be combined with the spell to
# result in a successful combination.
# Space complexity: O(m+n) - We sort both arrays, in Python it takes
# extra space.
#
# Runtime 1847 ms Beats 58.7%
# Memory 44.2 MB Beats 5.38%
class DiscardPrevious:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        # Sort both arrays.
        potions.sort()
        spells = [(spell, i) for i, spell in enumerate(spells)]
        spells.sort()
        n = len(potions)
        res = [0] * len(spells)
        prev_right = n
        for spell_force, i in spells:
            # Left pointer points to the right-most known non-successful
            # potion, right points to the left-most known
            # successful potion,
            l, r = 0, prev_right
            while l < r:
                mid = (l + r) // 2
                combined_force = spell_force * potions[mid]
                if combined_force < success:
                    l = mid + 1
                else:
                    r = mid
            res[i] = n - r
            prev_right = r
        return res


def test():
    executors = [
        BuiltInBisect,
        BinarySearchPotions,
        DiscardPrevious,
    ]
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    with open(
        os.path.join(
            __location__, "successful-pairs-of-spells-and-potions.json"
        )
    ) as json_file:
        tests = json.load(json_file)
        for executor in executors:
            start = timeit.default_timer()
            for _ in range(1):
                for col, t in enumerate(tests):
                    sol = executor()
                    result = sol.successfulPairs(t[0], t[1], t[2])
                    exp = t[3]
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
