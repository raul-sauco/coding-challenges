# Valid Starting City
# 🟠 Medium
#
# https://www.algoexpert.io/questions/valid-starting-city
#
# Tags: Array - Greedy

import timeit


# The valid starting city will be the one right after the point at which
# our gas deficit is at its highest, we just need to find that point and
# return the index following it.
#
# Time complexity: O(n) - We visit each position once.
# Space complexity: O(1) - We only use constant space.
class Solution:
    def validStartingCity(self, distances, fuel, mpg) -> int:
        # Find the point at which our fuel deficiency is the highest.
        current = fuel[0] * mpg - distances[0]
        worst = (0, current)
        for i in range(1, len(distances)):
            # Add the amount of fuel we obtain by stopping here minus
            # the distance we need to cover to the next gas station.
            current += fuel[i] * mpg - distances[i]
            if current < worst[1]:
                worst = (i, current)
        return (worst[0] + 1) % len(distances)


def test():
    executors = [Solution]
    tests = [
        [[10, 10, 10, 10], [1, 2, 3, 4], 4, 2],
        [[5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10, 4],
        [[15, 20, 25, 30, 35, 5], [0, 3, 0, 0, 1, 1], 26, 5],
        [[10, 20, 10, 15, 5, 15, 25], [0, 2, 1, 0, 0, 1, 1], 20, 1],
        [[1, 3, 10, 6, 7, 7, 2, 4], [1, 1, 1, 1, 1, 1, 1, 1], 5, 6],
        [
            [30, 40, 10, 10, 17, 13, 50, 30, 10, 40],
            [1, 2, 0, 1, 1, 0, 3, 1, 0, 1],
            25,
            1,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.validStartingCity(t[0], t[1], t[2])
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
