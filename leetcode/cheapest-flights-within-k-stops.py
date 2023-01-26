# 787. Cheapest Flights Within K Stops
# 🟠 Medium
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
#
# Tags: Dynamic Programming - Depth-First Search - Breadth-First Search
# Graph - Heap (Priority Queue) - Shortest Path

import timeit
from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List


# Use a modified version of Dijkstra where instead of storing one only
# distance to each node in the graph, we store a multidimensional array
# of best distances having used k stops. As we Dijkstra, we use a heap
# to explore shorter paths first but in this case, we can visit the same
# node multiple times, as long as the number of stops is different,
# because a more expensive route may require less stops and it may lead
# to the solution.
#
# Time complexity: O(n*log(n)) - Creating the adjacency list can be done
# in O(n), where n is the number of flights, but exploring the graph may
# lead to each flight being pushed and popped from the heap in O(log(n)).
# Space complexity: O(n) - All the flights will be stored in the
# adjacency list, and the heap may also grow to size n, for example if
# we could visit all the cities from the origin.
#
# Runtime: 449 ms, faster than 38.94%
# Memory Usage: 16.5 MB, less than 6.89%
class Dijkstra:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = defaultdict(dict)
        for source, dest, price in flights:
            adj[source][dest] = price
        # Store the optimal prices to get to city n having used k stops.
        prices = [[float("inf")] * (k + 1) for _ in range(n)]
        # optimal_prices[src] = 0
        # Start at the destination, the first cities we land at will
        # have required 0 stops.
        heap = [(0, -1, src)]
        while heap:
            trip_price, stops, city = heappop(heap)
            # The first time we pop a city from the heap it will have
            # the ideal travel time but we may need to wait for a less
            # optimal travel time with less stops.
            if trip_price < prices[city][stops]:
                prices[city][stops] = trip_price
                # Dijkstra guarantees that the first path to get to the
                # destination will be the shortest (cheapest).
                if city == dst:
                    return trip_price
                for dest, leg_price in adj[city].items():
                    if stops < k:
                        heappush(
                            heap, (trip_price + leg_price, stops + 1, dest)
                        )
        return -1


# Use Bellman-Ford's algorithm, store the minimum distance to reach each
# city in an array and explore all the edges k+1 times, for each edge,
# if we can reach the destination at a cheaper price than previously,
# update the price.
#
# Time complexity: O(m*k) - Where m is the number of flights in the
# input, we iterate k+1 times over all the flights.
# Space complexity: O(n) - The prices array has size n.
#
# Runtime: 268 ms, faster than 58.75%
# Memory Usage: 15.1 MB, less than 89.54%
class BellmanFord:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            tmp = prices[:]
            for source, dest, price in flights:
                if prices[source] == float("inf"):
                    continue
                tmp[dest] = min(tmp[dest], prices[source] + price)
            prices = tmp
        return -1 if prices[dst] == float("inf") else prices[dst]


# We can travel one node at a time, and at most k + 1 nodes from the
# source, also, once we get to the destination, we have a ceiling in
# how much an itinerary can cost before we decide that it is not worth
# pursuing it any longer. All that means that we can use BFS to explore
# one level at a time, we start by flying from the source to all
# available destinations, then, from all of them to all the ones that
# we can reach from there and so on, if the price to get to a destination
# is greater than a price that we have seen before, with least stops, we
# discard that branch, if the price of a trip becomes greater than the
# cheapest way to get to dst found so far, we discard it as well, we
# run the BFS algorithm k+1 times, then return the solution or -1.
#
# Time complexity: O(n*k) - The outer loop runs k times, the inner loop
# will average n items maximum because we only enqueue elements when we
# find a cheaper path in a later iteration.
# Space complexity: O(f) - Where f is the number of flights, we save all
# flight information in the adjacency list.
#
# Runtime 95ms Beats 98.82%
# Memory 15.1 MB Beats 73.37%
class BFS:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Create an adjacency list.
        adjacencies = defaultdict(list)
        for s, d, p in flights:
            adjacencies[s].append((d, p))
        queue = deque([(src, 0)])
        best = [float("inf")] * n
        for _ in range(k + 1):
            # If queue is empty, the next for loop will not run, we
            # don't need to protect here.
            # Process an entire level.
            for _ in range(len(queue)):
                f, cum_price = queue.popleft()
                for d, trip_price in adjacencies[f]:
                    ptd = cum_price + trip_price
                    # If this represents the best way to get to the
                    # destination so far and if this trip is not already
                    # more expensive than the best way to get to the dest.
                    if ptd < best[d] and ptd < best[dst]:
                        best[d] = ptd
                        # If this is the destination, the cost cannot
                        # improve traveling from there since there are no
                        # negatively weighted edges.
                        if d != dst:
                            queue.append((d, ptd))

        return best[dst] if best[dst] != float("inf") else -1


def test():
    executors = [
        Dijkstra,
        BellmanFord,
        BFS,
    ]
    tests = [
        [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200],
        [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500],
        [4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1, 6],
        [
            5,
            [
                [4, 1, 1],
                [1, 2, 3],
                [0, 3, 2],
                [0, 4, 10],
                [3, 1, 1],
                [1, 4, 3],
            ],
            2,
            1,
            1,
            -1,
        ],
        [
            4,
            [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]],
            0,
            3,
            1,
            700,
        ],
        [
            7,
            [
                [0, 3, 7],
                [4, 5, 3],
                [6, 4, 8],
                [2, 0, 10],
                [6, 5, 6],
                [1, 2, 2],
                [2, 5, 9],
                [2, 6, 8],
                [3, 6, 3],
                [4, 0, 10],
                [4, 6, 8],
                [5, 2, 6],
                [1, 4, 3],
                [4, 1, 6],
                [0, 5, 10],
                [3, 1, 5],
                [4, 3, 1],
                [5, 4, 10],
                [0, 1, 6],
            ],
            2,
            4,
            1,
            16,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findCheapestPrice(t[0], t[1], t[2], t[3], t[4])
                exp = t[5]
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
