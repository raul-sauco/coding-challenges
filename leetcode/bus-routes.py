# 815. Bus Routes
# 🔴 Hard
#
# https://leetcode.com/problems/bus-routes/
#
# Tags: Array - Hash Table - Breath-First Search

import timeit
from collections import deque
from typing import List


# Create a dictionary that stores the minimum number of stops needed to
# reach a given destination. Iterate once over the bus list adding
# every bus, except the one we can reach from the initial stop, if
# there is one, to a queue of buses waiting to be processed.
# Start processing buses from the queue, we will be able to reach the
# bus if one of its stops is reachable, then we can add that bus stops
# to the dictionary of reachable bus stops.
# If during one loop the queue does not decrease in size, we can exit
# the loop and return -1, we won't be able to reach any more stops.
#
# Time complexity: O(n^2) - n: number of bus stops. The number of times
# we will visit each bus stop has a relation with the ordering of the
# routes, if the input was already ordered in the way we would travel
# through the bus routes, we would only need to visit each bus stop once
# O(n) time complexity, but if the only route we could visit each time
# was the last one on the queue, we would visit each bus stop before
# adding the last one, on each loop, O(n^2)
# Space complexity: O(n) - Both the dictionary and the queue will have
# the same size as the input.
#
# Runtime: 656 ms, faster than 71.60%
# Memory Usage: 29.9 MB, less than 91.27%
class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        # Add the first stop to the dictionary, we don't need to take
        # any bus to get there.
        dp = {source: 0}
        # Add all the routes to the queue.
        queue = deque(routes)
        # Detect when we have gone through all the elements of the queue
        # without making any progress.
        to_process = len(queue)
        # While there are routes to process and we haven't seen them all
        # without making any progress.
        while to_process:
            route = queue.popleft()
            # Save the minimum number of stops in which we can reach
            # the route.
            steps_to_reach = float("inf")
            for stop in route:
                if stop in dp:
                    steps_to_reach = min(steps_to_reach, dp[stop])
            # If we can reach, add all the stops to the dictionary.
            if steps_to_reach != float("inf"):
                # Restart the counter of elements that we can visit.
                to_process = len(queue)
                for stop in route:
                    if stop in dp:
                        # If we could already reach this stop, store the
                        # quickest way to get there.
                        dp[stop] = min(dp[stop], steps_to_reach + 1)
                    else:
                        dp[stop] = steps_to_reach + 1
            # If we didn't manage to reach that bus route on this
            # iteration, readd it and and 1 to the number of routes of
            # the current queue that we have seen.
            else:
                queue.append(route)
                to_process -= 1

        # If we found a way to get to this stop return the number of
        # buses we took, otherwise -1.
        if target in dp:
            return dp[target]
        return -1


def test():
    executors = [Solution]
    tests = [
        [[[1, 2, 7], [3, 6, 8]], 1, 6, -1],
        [[[1, 2, 7], [3, 6, 7]], 1, 6, 2],
        [[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12, -1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.numBusesToDestination(t[0], t[1], t[2])
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
