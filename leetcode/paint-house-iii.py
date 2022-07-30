# 1473. Paint House III
# 🔴 Hard
#
# https://leetcode.com/problems/paint-house-iii/
#
# Tags: Array - Dynamic Programming


import timeit
from functools import cache
from typing import List


# Explore all the options recursively saving intermediate results using
# lru_cache
#
# - Paint each house with each color available
# - Check if the resulting array satisfies target
# - Out of the ones that satisfy target, return the one with the minimum
# cost.
#
# Time complexity: O(m*t*n^3)
# Space complexity: O(m*t*n^2)
#
# This solution would fail with Time Limit Exceeded.
class BruteForce:
    def minCost(
        self,
        houses: List[int],
        cost: List[List[int]],
        m: int,
        n: int,
        target: int,
    ) -> int:
        def countGroups(state: tuple[int]) -> int:
            count = 0
            last = 0
            for item in state:
                if item != last:
                    last = item
                    count += 1
            return count

        def paintWithColor(
            row: tuple[int], idx: int, color: int
        ) -> tuple[int]:
            result = [x for x in row]
            result[idx] = color
            return tuple(result)

        def paint(state: tuple[int], i: int):
            best = float("inf")
            if state[i] == 0:
                for j, c in enumerate(cost[i]):
                    # Add the cost of painting this house with this
                    # color to the return
                    price = -1
                    painted = paintWithColor(state, i, j + 1)

                    # If we are not looking at the last item, check
                    #  whether the suffix can be computed
                    if i < len(houses) - 1:
                        suffix_price = paint(painted, i + 1)
                        # If we could paint the suffix array
                        if suffix_price != -1:
                            price = c + suffix_price

                    # If we are computing the last item, check whether
                    # it matches the target
                    elif countGroups(painted) == target:
                        price = c
                    # Only accept the price if the target is satisfied
                    if price != -1:
                        best = min(price, best)

                if best == float("inf"):
                    return -1
                return best

            # state[i] is not 0, this house is already painted
            if i < len(houses) - 1:
                return paint(state, i + 1)
            else:
                # This is the last element
                if countGroups(state) == target:
                    return 0
                return -1

        return paint(tuple(houses), 0)


# Improve on the brute-force solution by memoizing intermediate results
# as defined in the second hind of the description.
#
# Time complexity: O(m*t*n^2) - We may call n times dfs with the same
# arguments. TC = SC * n.
# Space complexity: O(m*t*n) - The number of different value
# combinations that the memoized function can take. The complexity comes
# from the call stack.
#
# Runtime: 435 ms, faster than 96.95% of Python3 online submissions for
# Paint House III.
# Memory Usage: 20.4 MB, less than 55.88% of Python3 online submissions
# for Paint House III.
class Memoization:
    def minCost(
        self,
        houses: List[int],  # List of input house colors. 0 == paint.
        cost: List[List[int]],  # 2D matrix [house, cost].
        num_houses: int,
        num_colors: int,
        target_num_neighborhoods: int,
    ) -> int:

        # The function arguments (i, j, k) represent the minimum cost to
        # - paint the last i houses
        # - with k neighborhoods
        # - and house at index i - 1 is color j
        # Memoize intermediate results using functools.cache (v >= 3.9)
        @cache
        def dfs(house_idx, last_color, num_neighborhoods):
            # Clean the search space returning fast from calls that
            # cannot lead to a solution.
            # k < 0 - We have used up the target number of neighborhoods
            # m-i<k - We have too many neighborhoods and will not be
            if (
                num_neighborhoods < 0
                or num_houses - house_idx < num_neighborhoods
            ):
                return float("inf")

            # Base case, we have painted all the houses and we have the
            # correct number of neighborhoods, return 0 and the return
            # calls going backwards in the call stack will add the cost
            # of painting the other houses.
            if num_neighborhoods == 0 and house_idx == len(houses):
                return 0

            # If the house was not painted the previous year, i.e. we
            # need to paint it, explore the possible sub-trees and
            # return the one with the minimum cost.
            if houses[house_idx] == 0:
                # For each possible color, calculate the minimum cost
                # of painting the next houses if the current house was
                # that color, add the cost of painting this house on
                # that color, and return that value.
                return min(
                    dfs(
                        house_idx + 1,
                        color,
                        num_neighborhoods - (color != last_color),
                    )
                    + cost[house_idx][color - 1]
                    for color in range(1, num_colors + 1)
                )
            else:
                # If we cannot paint the house, move onto the next house
                # and calculate the minimum cost from there.
                return dfs(
                    house_idx + 1,
                    houses[house_idx],
                    num_neighborhoods - (houses[house_idx] != last_color),
                )

        res = dfs(0, -1, target_num_neighborhoods)
        # If res == float("inf") we could not find a way to paint the
        # houses with the given number of neighborhoods, return -1
        # We cannot use -1 as the return for dfs because we need to be
        # able to return the minimum cost between different return
        # values, by returning float("inf") when we fail, we make sure
        # that we will prioritize valid values.
        return res if res < float("inf") else -1


def test():
    executors = [
        BruteForce,
        Memoization,
    ]
    tests = [
        [
            [0, 0, 0, 0, 0],
            [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
            5,
            2,
            3,
            9,
        ],
        [
            [0, 2, 1, 2, 0],
            [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]],
            5,
            2,
            3,
            11,
        ],
        [
            [3, 1, 2, 3],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
            4,
            3,
            3,
            -1,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for idx, t in enumerate(tests):
                sol = executor()
                result = sol.minCost(t[0], t[1], t[2], t[3], t[4])
                exp = t[5]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {idx} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
