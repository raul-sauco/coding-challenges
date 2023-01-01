# Stable Internships
# 🟠 Medium
#
# https://www.algoexpert.io/questions/stable-internships
#
# Tags: Famous Algorithms - Gale–Shapley

import timeit
from typing import List


# This problem is asking us to implement the Gale-Shapley algorithm:
# https://en.wikipedia.org/wiki/Gale–Shapley_algorithm
#
# Time complexity: O(n^2) - Where n is the number of interns/teams.
# Space complexity: O(n) - The next_apply_at and teams dictionaries and
# the free interns set all use O(n) extra memory.
class Solution:
    def stableInternships(self, interns, teams) -> List[int]:
        n = len(interns)
        team_dict = {i: None for i in range(n)}
        next_apply_at = {i: 0 for i in range(n)}
        free_interns = {i for i in range(n)}
        while free_interns:
            intern = free_interns.pop()
            for idx in range(next_apply_at[intern], n):
                # We are applying to this company, do not apply again.
                next_apply_at[intern] = idx + 1
                team = interns[intern][idx]
                # This team has not found an intern yet, match them.
                if team_dict[team] is None:
                    team_dict[team] = intern
                    break  # Break out of matching this intern.
                else:
                    # The team has an intern already, check if they
                    # would prefer to have this intern instead.
                    team_current_intern = team_dict[team]
                    team_preferences = teams[team]
                    if team_preferences.index(intern) < team_preferences.index(
                        team_current_intern
                    ):
                        # The current intern becomes free.
                        free_interns.add(team_current_intern)
                        # Match this team with this intern.
                        team_dict[team] = intern
                        break  # Break out of matching this intern.
        return [[intern, team] for team, intern in team_dict.items()]


def test():
    executors = [Solution]
    tests = [
        [[[1, 0], [0, 1]], [[0, 1], [1, 0]], [[0, 1], [1, 0]]],
        [
            [[0, 1, 2], [2, 1, 0], [1, 2, 0]],
            [[2, 1, 0], [0, 1, 2], [0, 2, 1]],
            [[0, 0], [1, 2], [2, 1]],
        ],
        [
            [[0, 1, 2], [1, 0, 2], [1, 2, 0]],
            [[2, 1, 0], [1, 2, 0], [0, 2, 1]],
            [[0, 0], [1, 1], [2, 2]],
        ],
        [
            [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 3, 1], [0, 2, 3, 1]],
            [[1, 3, 2, 0], [0, 1, 2, 3], [1, 3, 2, 0], [3, 0, 2, 1]],
            [[0, 1], [1, 0], [2, 3], [3, 2]],
        ],
        [
            [[0, 1, 2, 3], [2, 1, 3, 0], [0, 2, 3, 1], [3, 1, 0, 2]],
            [[1, 3, 2, 0], [0, 1, 2, 3], [1, 2, 3, 0], [3, 0, 2, 1]],
            [[0, 1], [1, 2], [2, 0], [3, 3]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sorted(sol.stableInternships(t[0], t[1]))
                exp = sorted(t[2])
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
