# 948. Bag of Tokens
# 🟠 Medium
#
# https://leetcode.com/problems/bag-of-tokens/
#
# Tags: Array - Two Pointers - Greedy - Sorting

import timeit
from collections import deque
from typing import List


# Play the smallest tokens to gain score and the bigger ones to gain
# power, that way we can maximize the number of plays.
#
# Time complexity: O(n*log(n)) - Where n is the number of tokens. The
# sorting step has the highest cost, then we can play the tokens in O(n)
# Space complexity: O(n) - The queue has length n.
#
# Runtime: 90 ms, faster than 45.75%
# Memory Usage: 13.9 MB, less than 99.06%
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Initialize our score.
        score = 0
        # We want to access both the smallest and biggest element,
        # sort the tokens and use a deque to store them.
        q = deque(sorted(tokens))
        # Keep track of the length of the queue to determine whether we
        # made a move on the last round.
        last_token_count = len(q) + 1
        # Keep going while we have tokens and we made a move on the last
        # round.
        while q and len(q) < last_token_count:
            last_token_count = len(q)
            # If we can score, do it greedily.
            if power >= q[0]:
                # Play face up.
                power -= q.popleft()
                score += 1
            # If we can play a token face down (score > 0) and we are
            # not going to loose points doing so, play the biggest token
            # face down.
            elif score and len(q) > 1:
                # Play the biggest token face down.
                power += q.pop()
                score -= 1
        # Return the result.
        return score


def test():
    executors = [Solution]
    tests = [
        [[], 200, 0],
        [[100], 50, 0],
        [[100, 200], 150, 1],
        [[100, 200, 300, 400], 200, 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.bagOfTokensScore(t[0], t[1])
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
