# Apartment Hunting
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/apartment-hunting
#
# Tags: Array

import timeit


# The naive solution would visit each block and compute the distances to
# all required facilities without taking into account any of the
# previous calculations, that would be O(n^2*r) with n the number of
# blocks and r the number of requirements. We can improve that using a
# greedy approach, we do one pass left to right computing the distances
# that we need to walk from each block to each requirement if we went
# west from the blocks, if a block has that requirement, the distance
# is 0, otherwise, the distance equals the distance from the previous
# block + 1, we can do that in O(n*r), then we do the same going
# right to left and checking if we can get to any of the facilities
# quicker walking east, if we can, we update the value, we also compute
# the maximum distance that we need to walk from the current block to
# the furthest away facility inside this loop and keep a variable with
# the best block to move into.
#
# Time complexity: O(n*r) - Two passes over the blocks checking all the
# requirements for each.
# Space complexity: O(n*r) - We keep a list of size n with each entry
# a dictionary of size r where the values are the distance to the
# closest required facility from the given block.
class Solution:
    def apartmentHunting(self, blocks, reqs):
        # Store the minimum costs of reaching each required facility
        # from each block.
        costs = [{req: float("inf") for req in reqs} for _ in blocks]
        for i, block in enumerate(blocks):
            for req in reqs:
                # If this block has this facility, the cost of getting
                # there is 0.
                if block[req]:
                    costs[i][req] = 0
                # If it doesn't have it, the cost of getting there
                # going west is the cost of getting there from the
                # previous building + 1. This works for the first
                # building as well because it compares with the
                # infinity values of the last building.
                else:
                    costs[i][req] = costs[i - 1][req] + 1
        # Now check the best distances traveling east and keep the index
        # of the best block to move to. (total cost, index)
        best = (max(costs[-1].values()), len(costs) - 1)
        for i in range(len(blocks) - 2, -1, -1):
            block = blocks[i]
            # What is the furthest you need to walk to get to any of
            # the required facilities.
            furthest = 0
            # Can we get there faster going east rather than west?
            for req in reqs:
                costs[i][req] = min(costs[i][req], costs[i + 1][req] + 1)
                furthest = max(furthest, costs[i][req])
            if furthest < best[0]:
                best = (furthest, i)
        return best[1]


def test():
    executors = [Solution]
    tests = [
        [
            [
                {"gym": False, "school": True, "store": False},
                {"gym": True, "school": False, "store": False},
                {"gym": True, "school": True, "store": False},
                {"gym": False, "school": True, "store": False},
                {"gym": False, "school": True, "store": True},
            ],
            ["gym", "school", "store"],
            3,
        ],
        [
            [
                {
                    "foo": True,
                    "gym": False,
                    "kappa": False,
                    "office": True,
                    "school": True,
                    "store": False,
                },
                {
                    "foo": True,
                    "gym": True,
                    "kappa": False,
                    "office": False,
                    "school": False,
                    "store": False,
                },
                {
                    "foo": True,
                    "gym": True,
                    "kappa": False,
                    "office": False,
                    "school": True,
                    "store": False,
                },
                {
                    "foo": True,
                    "gym": False,
                    "kappa": False,
                    "office": False,
                    "school": True,
                    "store": False,
                },
                {
                    "foo": True,
                    "gym": True,
                    "kappa": False,
                    "office": False,
                    "school": True,
                    "store": False,
                },
                {
                    "foo": True,
                    "gym": False,
                    "kappa": False,
                    "office": False,
                    "school": True,
                    "store": True,
                },
            ],
            ["gym", "school", "store"],
            5,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.apartmentHunting(t[0], t[1])
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
