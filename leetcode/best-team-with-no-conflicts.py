# 1626. Best Team With No Conflicts
# 🟠 Medium
#
# https://leetcode.com/problems/best-team-with-no-conflicts/
#
# Tags: Array - Dynamic Programming - Sorting

import timeit
from typing import List


# Create a sorted array of players represented by (score, age) then we
# can iterate over them, a max of 1000 iterations. We will keep a dp
# structure with the best total score that we have been able to find
# for a given maximum age, for each player, we iterate over the dp
# structure, if the oldest player is of the same age or younger than the
# current player, we could add this player to the team.
#
# Time complexity: O(n*1000) - For small values of n this will be
# the same as n^2, but for larger values of n it can be simplified as
# O(n*log(n)) because then the sorting step, instead of the loops, could
# present the highest complexity , we get this complexity sorting by
# score and using age as the key of the dp.
# Space complexity: O(n) - The sorted players array has the same size as
# the input, the dp structure could as well grow to the same size.
#
# Runtime 1989 ms Beats 63.83%
# Memory 14.2 MB Beats 51.77%
class DP:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Sort by scores first and ages later, then use ages for dp.
        sa = sorted(zip(scores, ages))
        dp = {0: 0}
        # O(n) Iterate over all players, they are sorted already in
        # order of ascending scores, we need to check that we don't add
        # a player younger than the oldest in the branch.
        for score, age in sa:
            # O(1000)
            for oldest_in_branch, total_score in dp.copy().items():
                # If this player is at least as old as the oldest in the
                # given branch, we could add them.
                if oldest_in_branch <= age:
                    key = max(oldest_in_branch, age)
                    value = total_score + score
                    if key not in dp:
                        dp[key] = value
                    else:
                        dp[key] = max(dp[key], value)

        return max(dp.values())


# Once we sort the players by score, this problem becomes obtaining the
# sum of scores of players up to, and including, a given age that we
# have seen already. That makes this problem similar to range sum
# query mutable in that we need to efficiently update elements in an
# array and query sum ranges at that point, before we add any player
# with a higher score.
#
# Time complexity: O(n*log(a)) - Where n is the number of players and a
# is the max age in the input and it is limited to a max a 1000.
# Space complexity: O(n) - The sorted players array has the same size as
# the input, the binary indexed tree has size max(ages).
#
# Runtime 230 ms Beats 98.58%
# Memory 14.1 MB Beats 99.29%
class BITSolution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Sort by scores first and ages later, then use ages for dp.
        sa = sorted(zip(scores, ages))
        # Initialize an array to be used as the binary indexed tree.
        bit = [0] * (max(ages) + 1)
        # Define a function that updates the binary indexed tree with
        # the best score currently possible using players up to age age.
        def updateBIT(age: int, score: int) -> int:
            # First update the value in the tree.
            idx = age
            while idx < len(bit):
                bit[idx] = max(bit[idx], score)
                idx += idx & (-idx)

        # Get the best score of a team composed of members up to and
        # including age.
        def queryBIT(age: int) -> int:
            idx = age
            best = 0
            while idx > 0:
                best = max(best, bit[idx])
                idx -= idx & (-idx)
            return best

        res = 0
        for score, age in sa:
            best_score = score + queryBIT(age)
            # Use the best possible score with this max age to update
            # the bit.
            updateBIT(age, best_score)
            res = max(res, best_score)
        return res


def test():
    executors = [
        # DP,
        BITSolution,
    ]
    tests = [
        [[4, 5, 6, 5], [2, 1, 2, 1], 16],
        [[1, 2, 3, 5], [8, 9, 10, 1], 6],
        [[1, 3, 5, 10, 15], [1, 2, 3, 4, 5], 34],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.bestTeamScore(t[0], t[1])
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
