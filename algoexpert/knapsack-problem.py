# Knapsack Problem
# 🔴 Hard
#
# https://www.algoexpert.io/questions/knapsack-problem
#
# Tags: Array - Dynamic Programming

import timeit
from typing import List


# Use an array of len == capacity + 1 where each item represents the
# maximum value that we can put in the knapsack when the knapsack's
# weight is equal to the position's index, for example dp[4] has the
# maximum profit found at the moment for a knapsack weight of 4 units.
# We iterate over the items, for each, we do a nested loop over all the
# values of capacity in reverse, from capacity to 0, what we are trying
# to do is check if we could add the item that we are visiting to a
# previous combination of items to come up with the weight k, if we can,
# we then check if using this new combination would result in a better
# profit, still for the same weight k, if it would, we then record this
# new "winning" combination in dp[k]. This problem has the added concern
# over the typical knapsack problem that they require us to store the
# indexes of the items that we are using, we can do that using a tuple
# of (int, List[int]) instead of a plain int as the values in dp.
#
# Time complexity: O(c*n) - Where c is the capacity given in the input
# and n is the number of items. For each item, we need to iterate the
# entire dp array, with c+1 positions. We could improve the complexity
# sorting the items array by weight and breaking out of the inner loop
# earlier, but we would need to store then the original element's index.
# Space complexity: O(c) - We store an extra array of size capacity.
class Solution:
    def knapsackProblem(self, items: List[int], capacity: int) -> int:
        res = [0, []]
        # dp is a list of tuples where the first item is the value
        # in the knapsack and the second is a list of the indexes used
        # to get that value for this weight and the index is the weight.
        dp = [res] + [None] * capacity
        # Iterate over all the items checking the combinations that we
        # can obtain adding them with other objects.
        for idx, item in enumerate(items):
            value, weight = item
            # Iterate over the dp object in reverse to avoid adding the
            # same item multiple times.
            for k in range(len(dp) - 1, -1, -1):
                # Can we get to dp[k] adding weight from dp[i] ?.
                i = k - weight
                if i >= 0 and dp[i] is not None:
                    # The result of adding this item to this knapsack has
                    # to be better than the previous best if any.
                    add_value = dp[i][0] + value
                    if dp[k] is None or dp[k][0] < add_value:
                        dp[k] = (add_value, dp[i][1] + [idx])
                        if add_value > res[0]:
                            res = list(dp[k])
        # Return the best combination of items.
        return res


def test():
    executors = [Solution]
    tests = [
        [[[1, 2], [4, 3], [5, 6], [6, 7]], 10, [10, [1, 3]]],
        [[[1, 2], [4, 3], [5, 6], [6, 9]], 11, [10, [0, 1, 2]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.knapsackProblem(t[0], t[1])
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
