# 2225. Find Players With Zero or One Losses
# 🟠 Medium
#
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
#
# Tags: Array - Hash Table - Sorting - Counting

import timeit
from collections import Counter
from typing import List


# The most adaptable solution is to use two counters to store all wins
# and loses of all the given players, then we can produce any results
# required based on the counters, for example, we could return all the
# players in order of more wins or "points".
#
# Time complexity: O(n*log(n)) - The players need to be sorted before
# being returned.
# Space complexity: O(n) - The counters can grow to size n.
#
# Runtime: 4867 ms, faster than 21.40%
# Memory Usage: 68.8 MB, less than 58.91%
class UseCounter:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        won, lost = Counter(), Counter()
        for w, l in matches:
            won[w] += 1
            lost[l] += 1
        return [
            sorted(set(won.keys() - set(lost.keys()))),
            sorted(x for x in lost.keys() if lost[x] == 1),
        ]


# Theoretical complexity can be improved if we use the count sort
# concept and an array to store intermediate results. We use the players
# ids as keys for the array and store the number of win/losses for any
# player that we see, then iterate over that array to generate the
# results in the desired format.
#
# Time complexity: O(k+n) - Where n is the number of matches in the
# input and k is the maximum number of players given to us in the
# description, 10^5.
# Space complexity: O(k) - The array k where we store intermediate
# results.
#
# Runtime: 3712 ms, faster than 66.77%
# Memory Usage: 70.6 MB, less than 8.18%
class UseArray:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Initialize an array of the maximum number of players allowed
        # by the description.
        results = [-1] * 100_001
        # Iterate over the matches storing the results.
        for w, l in matches:
            if results[w] == -1:
                results[w] = 0
            if results[l] == -1:
                results[l] = 1
            else:
                results[l] += 1
        # Iterate over the results constructing the winners and one
        # match lost arrays.
        winners, losers = [], []
        for i in range(len(results)):
            if results[i] == 0:
                winners.append(i)
            elif results[i] == 1:
                losers.append(i)
        return [winners, losers]


def test():
    executors = [
        UseCounter,
        UseArray,
    ]
    tests = [
        [[[2, 3], [1, 3], [5, 4], [6, 4]], [[1, 2, 5, 6], []]],
        [
            [
                [1, 3],
                [2, 3],
                [3, 6],
                [5, 6],
                [5, 7],
                [4, 5],
                [4, 8],
                [4, 9],
                [10, 4],
                [10, 9],
            ],
            [[1, 2, 10], [4, 5, 7, 8]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findWinners(t[0])
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
