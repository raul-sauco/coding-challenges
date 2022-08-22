# 134. Gas Station
# 🟠 Medium
#
# https://leetcode.com/problems/gas-station/
#
# Tags: Array - Greedy

import timeit
from typing import List

# The brute force solution simply visits each of the stops and, from
# each of them, starts traveling to the next one until it either gets
# back to the start position or fails to reach the next position.
#
# Time complexity: O(n^2) - We visit each position and, for each, travel
# forward, possibly the entire input.
# Space complexity: O(1) - Constant space.
#
# This solution would fail with Time Limit Exceeded.
class BruteForce:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Base case.
        if len(gas) == 1:
            # Could we travel from this station back to itself?
            return -1 if gas[0] < cost[0] else 0
        # Visit each element and try to travel the whole loop.
        for idx in range(len(gas)):
            # Try to travel the whole circular loop.
            j = idx + 1
            # The initial amount of fuel.
            fuel = gas[idx] - cost[idx]
            while fuel >= 0:
                # Check if we have gone over the end of the input.
                if j == len(gas):
                    # If we have gone past the last element, restart.
                    j = 0
                    continue
                # Base case, we went the whole way. We know that there
                # is only one correct solution, this is the one.
                if j == idx:
                    return idx
                # If we haven't gone around, check the cost of this gas
                # station.
                fuel += gas[j] - cost[j]
                # Update the inner loop index
                j += 1
        # If we could not reach the destination from any starting
        # position, return -1
        return -1


# There is a key observation that can help us go from O(n^2) to O(n)
# time complexity, it has two components:
# We calculate the sums of the gas and cost arrays, if the sum of gas is
# less than the sum of costs, we will not be able to go all the way
# around, and we can return -1, otherwise we know that there is a
# solution. We start visiting the first element (it could be any
# element, but visiting i=0 first simplifies the code) and checking if
# we can travel to the next element, then keep doing this while we can
# reach the next element. If at some point we cannot reach the next
# element, we know that we have a gas deficiency in the section that we
# have visited already, that means that, if we take the remaining
# elements, there will be a gas surplus so, by starting at the first
# element after an element that has a negative gas - cost balance, we
# can be sure that we will be able to travel all the way around.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - Constant space.
#
# Runtime: 824 ms, faster than 74.70%
# Memory Usage: 19.1 MB, less than 77.68%
class Greedy:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if we have enough gas to cover the cost.
        if sum(gas) < sum(cost):
            return -1
        # We start with 0 gas.
        total_fuel = total_cost = fuel = 0
        # Initialize the result with the first element.
        res = 0
        for i in range(len(gas)):
            total_fuel += gas[i]
            total_cost += cost[i]
            fuel += gas[i] - cost[i]
            # If we can't reach the next position, that could be the
            # initial position of the successful loop.
            if fuel < 0:
                # Reset the fuel level, we are checking if we could
                # start from this position, we don't want to carry a
                # negative fuel count.
                fuel = 0
                # The next position could be the start of the loop.
                res = i + 1
        return res


# We can trade-off some memory for time if instead of computing and
# comparing the sums at the start of the algorithm, we compute the
# running sums of cost and gas at each iteration of the loop, then
# check if the total gas is equal or greater than the total cost before
# returning the result.
#
# Time complexity: O(n) - We visit each element once.
# Space complexity: O(1) - Constant space.
#
# Runtime: 702 ms, faster than 91.88%
# Memory Usage: 19.2 MB, less than 52.98%
class GreedyOneLoop:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # We start with 0 gas.
        total_fuel = total_cost = fuel = 0
        # Initialize the result with the first element.
        res = 0
        for i in range(len(gas)):
            total_fuel += gas[i]
            total_cost += cost[i]
            fuel += gas[i] - cost[i]
            # If we can't reach the next position, that could be the
            # initial position of the successful loop.
            if fuel < 0:
                # Reset the fuel level, we are checking if we could
                # start from this position, we don't want to carry a
                # negative fuel count.
                fuel = 0
                # The next position could be the start of the loop.
                res = i + 1
        return res if total_cost <= total_fuel else -1


def test():
    executors = [
        BruteForce,
        Greedy,
        GreedyOneLoop,
    ]
    tests = [
        [[4], [5], -1],
        [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3],
        [[2, 3, 4], [3, 4, 3], -1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.canCompleteCircuit(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
