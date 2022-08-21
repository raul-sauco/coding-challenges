# 871. Minimum Number of Refueling Stops
# 🔴 Hard
#
# https://leetcode.com/problems/minimum-number-of-refueling-stops/
#
# Tags: Array - Dynamic Programming - Greedy - Heap (Priority Queue)

import timeit
from heapq import heappop, heappush
from typing import List


# The brute force approach visits every station that can be reached with
# the current amount of fuel and, for each, decides to either refuel
# there or skip it.
#
# Time complexity: O(2^n) - With n being the number of gas stations, we
# choose to either visit or not visit each of them.
# Space complexity: O(n) - We can have n calls in the stack before they
# start returning results.
#
# This solution would fail with Time Limit Exceeded.
# We could easily memoized visitNext using @functools.cache but it would
# not help because most of the redundant work would still be done.
class BruteForce:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        # Define a function that explores the result of stopping and
        # skipping the next gas station and returns the one with the
        # least number of stops.
        # @param position: the current position.
        # @param fuel: the amount of fuel left.
        # @param idx: the idx of the gas station that we are considering
        # visiting or skipping.
        def visitNext(position: int, fuel: int, idx: int):
            # Base case, we have enough fuel to get to the target.
            if position + fuel >= target:
                # We don't need to do any more stops.
                return 0
            # Base case, we don't have enough fuel to get to the next
            # gas station we are trying to get to, or we are out of gas
            # stations where we can refuel.
            if idx == len(stations) or stations[idx][0] - position > fuel:
                return float("inf")
            # If we stop at this gas station, we start from the position
            # where the gas station is. Fuel is the current fuel minus
            # the fuel we use to get there plus the fuel at the gas
            # station, and the idx is the next gas station index.
            visit = (
                visitNext(
                    stations[idx][0],
                    fuel - (stations[idx][0] - position) + stations[idx][1],
                    idx + 1,
                )
                + 1
            )
            # If we skip this gas station, we try to get to the next one.
            skip = visitNext(position, fuel, idx + 1)
            # Return the option that has the least number of stops.
            return min(visit, skip)

        # Initial call.
        res = visitNext(0, startFuel, 0)
        # If we couldn't find a way to get to the target, return
        if res == float("inf"):
            return -1
        return res


# Keep a dp array with the index as the number of stops and the value
# being the farthest we can drive with idx number of stops. Visit each
# gas station and update the dp array backwards from its index to 0
# with the best distance for this number of stops between the current
# best and the best distance with one less stop plus the amount of gas
# available at this station.
#
# Time complexity: O(n^2) - With n the number of gas stations. We visit
# each gas station and for each, we visit all the previous ones inside
# a nested loop.
# Space complexity: O(n) - With n the number of gas stations, equal to
# the size of the dp array.
#
# Runtime: 1202 ms, faster than 19.44%
# Memory Usage: 14.3 MB, less than 10.13%
class DP:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        # Base case, we start with enough fuel to get to the target.
        if startFuel >= target:
            return 0
        # dp dictionary stores the furthest we can drive with key stops
        # for example, dp[3] will be the furthest we can drive with 3
        # refuelling stops. We initialize dp[0] with the initial gas.
        dp = [startFuel] + [0] * len(stations)
        # Iterate over the stations from closest to furthest away.
        for station_idx, (location, gas) in enumerate(stations):
            # For every station, iterate over all dp results from 0 to
            # the station's index, the maximum number of stops possible
            # at this point, in reverse order. [idx..0]
            for dp_idx in range(station_idx, -1, -1):
                # If we could have reached this gas station by stopping
                # at all previous ones along the way.
                if dp[dp_idx] >= location:
                    # Then, the furthest we can drive if we stop at this
                    # gas station is the maximum between previous
                    # results and the maximum driving distance before
                    # this stop plus the fuel stored at this station.
                    dp[dp_idx + 1] = max(dp[dp_idx + 1], dp[dp_idx] + gas)
        # Once we have calculated the maximum distance we can travel by
        # refueling n times for n in [0..len(stations) - 1], we have
        # to iterate over the dp array to find the first result that
        # lets us travel all the way to the target.
        for station_idx, d in enumerate(dp):
            if d >= target:
                return station_idx
        return -1


# It seems like there could be an optimization to the DP solution if
# instead of iterating over the dp array after the calculations, we
# stored the current shortest number of stops that lets us reach
# target and returned that after visiting all gas stations, but the
# code actually performs worst, probably because it checks the best
# O(n^2) times instead of iterating over the dp array in O(n) and
# returning the first match.
#
# Runtime: 2508 ms, faster than 5.15%
# Memory Usage: 14.2 MB, less than 74.58%


# A different approach than the evolution from brute force to dynamic
# programming of the previous solutions is based on greedy.
# We can make use of the fact that we don't need to decide if we stop
# or not at a gas station as we visit. We can "drive past" all of them,
# remembering the amount of gas that they had, until we "run out of gas"
# then add the gas at the station that we passed with the most gas, the
# best way of using one stop, to the current, and keep driving.
# The best way to keep track of which gas station, out of the ones that
# we have visited and not stopped at, has the most gas is using a heap.
#
# Time complexity: O(n*log(n)) - We visit each element and push it into
# the heap at O(log(n)), occasionally we pop from the heap to refuel.
# Even if we popped from the heap as often as we pulled the complexity
# would remain the same.
# Space complexity: O(n) - The heap can grow to the size of the input.
#
# Runtime: 214 ms, faster than 51.99%
# Memory Usage: 14.2 MB, less than 74.58%
class Heap:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        # Priority queue with the amount of gas in stations that we have
        # passed already and could have stopped at. Since Python only
        # has a min heap and we want the max gas, numbers are negated.
        skipped = []
        # Store the current position and the number of stops that we
        # have done already.
        position = stops = 0
        # Keep track of the current amount of fuel left.
        fuel = startFuel
        # Adding target to the array of stations to visit simplifies the
        # logic of the while loop. The problem guarantees that target is
        # greater than the position of any of the gas stations.
        stations.append([target, 0])
        # Start driving while we have fuel and we have not refuelled at
        # all stations.
        for location, gas in stations:
            # If we don't have enough gas to get to the next station,
            # pretend that we stopped at the skipped station with the
            # most gas.
            while position + fuel < location:
                # If there is no station available, we will not be
                # able to get to the end.
                if not skipped:
                    return -1
                # Else, pretend that we filled up at the gas station
                # with the most gas we drove past.
                fuel -= heappop(skipped)
                stops += 1
            # Once we exit the while loop, we have enough gas to drive
            # to the next station.
            # Subtract the gas we used.
            fuel -= location - position
            # Update our current position.
            position = location
            # Add the gas station to the heap in case we need it later.
            heappush(skipped, -gas)
        # Once we exit the loop, return the number of stops needed to
        # reach the target.
        return stops


def test():
    executors = [
        # BruteForce,
        DP,
        Heap,
    ]
    tests = [
        [1, 1, [], 0],
        [100, 1, [[10, 100]], -1],
        [100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2],
        [
            1000000,
            8663,
            [
                [31, 195796],
                [42904, 164171],
                [122849, 139112],
                [172890, 121724],
                [182747, 90912],
                [194124, 112994],
                [210182, 101272],
                [257242, 73097],
                [284733, 108631],
                [369026, 25791],
                [464270, 14596],
                [470557, 59420],
                [491647, 192483],
                [516972, 123213],
                [577532, 184184],
                [596589, 143624],
                [661564, 154130],
                [705234, 100816],
                [721453, 122405],
                [727874, 6021],
                [728786, 19444],
                [742866, 2995],
                [807420, 87414],
                [922999, 7675],
                [996060, 32691],
            ],
            6,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.minRefuelStops(t[0], t[1], t[2])
                exp = t[3]
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
