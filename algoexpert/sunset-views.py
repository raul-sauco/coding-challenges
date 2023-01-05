# Sunset Views
# 🟠 Medium
#
# https://www.algoexpert.io/questions/sunset-views
#
# Tags: Stack - Monotonic Stack - Greedy

import timeit


# Use the direction that the buildings face to determine in which
# direction to traverse the input. Store the height of the tallest
# building we have seen up to the moment, traverse all the buildings in
# the reversed order to where they face, when we see a taller building,
# we add it to the result set.
#
# Time complexity: O(n) - We visit each element in the input once.
# Space complexity: O(n) - The result list can grow to the same size as
# the input.
class Solution:
    def sunsetViews(self, buildings, direction):
        # A range object with the indexes to visit.
        rng = range(len(buildings))
        # If the buildings face east, we need to travel the input in
        # reversed order.
        if direction == "EAST":
            rng = reversed(rng)
        # Store the tallest building we have seen so far and the result.
        tallest, res = -1, []
        # Iterate over the buildings finding the ones that can see the
        # sunset because they are not blocked by others.
        for i in rng:
            if buildings[i] > tallest:
                res.append(i)
                tallest = buildings[i]
        # If we traveled the input in reverse, reverse the result to
        # have it sorted in ascending order. O(n).
        if direction == "EAST":
            res.reverse()
        return res


def test():
    executors = [Solution]
    tests = [
        [[3, 5, 4, 4, 3, 1, 3, 2], "EAST", [1, 3, 6, 7]],
        [[3, 5, 4, 4, 3, 1, 3, 2], "WEST", [0, 1]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.sunsetViews(t[0], t[1])
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
