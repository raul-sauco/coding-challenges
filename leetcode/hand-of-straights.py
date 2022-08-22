# 846. Hand of Straights
# 🟠 Medium
#
# https://leetcode.com/problems/hand-of-straights/
#
# Tags: Array - Hash Table - Greedy - Sorting

import timeit
from collections import Counter
from typing import List


# This problem seems similar to LeetCode 659. Split Array into
# Consecutive Subsequences, we can try a similar approach using a
# frequencies dictionary and greedily trying to build the sequences
# of length groupSize.
#
# Time complexity: O(n*log(n)) - Sorting has the biggest complexity,
# then we visit each card a maximum of two times for O(n).
# Space complexity: O(n) - The frequencies dictionary.
#
# Runtime: 210 ms, faster than 95.48%
# Memory Usage: 15.7 MB, less than 75.38%
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Sorting the input we make sure we visit smaller values first.
        hand.sort()
        # Store the frequencies of the elements we have available.
        available = Counter(hand)
        # Iterate over the sorted cards and try to build a sequence of
        # length group size.
        for card in hand:
            # Check if we have used all the cards of that value already.
            if available[card] <= 0:
                continue
            # We have, at least, one card of this value available, try
            # to build a sequence starting at this card.
            for i in range(groupSize):
                val = card + i
                # If we are missing any of the cards to build this
                # sequence, we have failed already.
                if available[val] <= 0:
                    return False
                # Register the fact that we are using one card of this
                # value.
                available[val] -= 1
        # If we manage to place all cards in sequences, we succeeded.
        return True


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True],
        [[1, 2, 3, 4, 5], 4, False],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.isNStraightHand(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
