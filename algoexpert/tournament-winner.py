# Tournament Winner
# 🟢 Easy
#
# https://www.algoexpert.io/questions/tournament-winner
#
# Tags: Array

import timeit
from collections import Counter


# The cleanest solution uses collections.Counter. I tried to shorten it
# using list comprehension but could not see how to do it.
#
# Time complexity: O(m) - With m the number of competitions, we visit
# each competition and result on the input once.
# Space complexity: O(n) - With n the number of teams, we will store
# one entry on the counter for each team.
class Solution:
    def tournamentWinner(self, competitions, results):
        c = Counter()
        for i in range(len(competitions)):
            # Since points are either 3 or 0, using 3 or 1 does not
            # change anything.
            c[competitions[i][results[i] - 1]] += 1
        return c.most_common()[0][0]


# The cleanest solution uses collections.Counter. I tried to shorten it
# using list comprehension but could not see how to do it.
#
# Time complexity: O(m) - With m the number of competitions, we visit
# each competition and result on the input once.
# Space complexity: O(n) - With n the number of teams, we will store
# one entry on the counter for each team.
class Solution2:
    def tournamentWinner(self, competitions, results):
        c = {}
        winner = (None, 0)
        for i in range(len(competitions)):
            team = competitions[i][results[i] - 1]
            if team not in c:
                c[team] = 1
            else:
                c[team] += 1
            if c[team] > winner[1]:
                winner = (team, c[team])
        return winner[0]


def test():
    executors = [
        Solution,
        Solution2,
    ]
    tests = [
        [
            [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]],
            [0, 0, 1],
            "Python",
        ],
        [
            [
                ["HTML", "Java"],
                ["Java", "Python"],
                ["Python", "HTML"],
                ["C#", "Python"],
                ["Java", "C#"],
                ["C#", "HTML"],
            ],
            [0, 1, 1, 1, 0, 1],
            "C#",
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.tournamentWinner(t[0], t[1])
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
