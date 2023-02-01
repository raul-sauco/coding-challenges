# Airport Connections
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/airport-connections
#
# Tags: Graphs

import timeit
from collections import defaultdict


# Start by marking all airports as unreachable, use the airports and
# routes to create an adjacency list that represents the graph and
# create a queue/stack of airports that are reachable but we have not
# visited yet. Start by adding the starting airport plus any airports
# that do not have any incoming flights to the stack. Then we start
# processing airports. For each airport on the stack, we recursively
# visit all their neighbors marking them as reachable, any time we
# run out of airports to visit, we pick one of the unreachable airports
# and add one to the count of flights that we need to add, then start
# visiting neighbors for that airport recursively. The result is the
# sum of airports that had no incoming flights, and were added at the
# beginning, plus the ones that were added when we run out of airports
# to visit during the DFS.
#
# Time complexity: O(r + a^2*log(a))
# Space complexity: O(r + a) - The adjacency list will have r entries, the
# missing set and stack could grow to size a.
class Solution:
    def airportConnections(self, airports, routes, startingAirport):
        # A function that takes in the name of an airport and returns
        # the number of unreachable airports that we can reach from it.
        def getScore(airport: str) -> int:
            seen = set(airport)
            stack = [airport]
            score = 0
            while stack:
                current = stack.pop()
                for nei in adj[current]:
                    if nei in unreachable and nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
                        score += 1
            return score

        # Build an adjacency list.
        adj = defaultdict(set)
        # The number of flights in and out of an airport.
        in_out = {a: [0, 0] for a in airports}
        # Initialize the count of flights that need to be added.
        extra_flights = 0
        for s, d in routes:
            adj[s].add(d)
            in_out[s][1] += 1
            in_out[d][0] += 1
        # Airports that we have no route to yet, a.k.a: unreachable.
        unreachable = set(airports)
        # We need to visit the starting airport.
        unreachable.remove(startingAirport)
        stack = [startingAirport]
        # We also need to visit any airports that do not currently have
        # any incoming flights, that means we need to create a flight to
        # them, lets visit them from the starting airport directly, that
        # way we can mark any airport that we can reach from any of them
        # as reachable as well.
        for airport in airports:
            incoming, _ = in_out[airport]
            if not incoming and airport != startingAirport:
                stack.append(airport)
                unreachable.remove(airport)
                extra_flights += 1
        # While we have not yet visited all airports.
        while unreachable:
            # If we have any airports to visit in the stack.
            if stack:
                source = stack.pop()
                for nei in adj[source]:
                    # We can visit this airport with the existing
                    # flights.
                    if nei in unreachable:
                        unreachable.remove(nei)
                        stack.append(nei)
            # If we have exhausted the list of airports that we can
            # reach, we need to create a new flight.
            else:
                extra_flights += 1
                stack.append(
                    sorted([(getScore(a), a) for a in unreachable]).pop()[1]
                )
        return extra_flights


# I do not have a proof for the correctness of this solution and I
# actually think that it is incorrect and we could create test cases
# that make the tests fail, even so, it is an interesting solution and I
# thought that it made sense saving it and look into its correctness
# later. It does pass the tests in AlgoExpert at the current date.
# The solution marks airports as visited using the list of airports that
# have been visited and their adjacency list to visit all airports that
# are reachable, since we know that flights that have no incoming flights
# will need a flight to them, we add them directly. Then we iterate
# over the remaining unreachable airports sorted ascending by number of
# incoming flights and descending by number of outgoing flights, that is
# to say, we prioritize airports with less incoming and more outgoing
# flights, and process them one at a time, marking all airports we can
# reach from them as reachable. This code may not always be correct but
# it is a much more efficient solution than the previous one and it
# could be an effective way to solve the problem with large inputs and a
# solution that is close enough to the optimal one.
#
# Time complexity: O(r + a*log(a)) - Sorting the unreachable airports by
# in and outdegree and traversing the routes to create the adjacency
# list are the most expensive steps, then we use at most O(n) to add
# and travel to the rest of airports because add each airport a maximum
# of one time to the stack.
# Space complexity: O(r+a) - The adjacency list will have r entries, the
# missing set and stack could grow to size a.
class DoNotUse:
    def airportConnections(self, airports, routes, startingAirport):
        # Build an adjacency list.
        adj = defaultdict(set)
        # The number of flights in and out of an airport.
        in_out = {a: [0, 0] for a in airports}
        # Initialize the count of flights that need to be added.
        extra_flights = 0
        for s, d in routes:
            adj[s].add(d)
            in_out[s][1] += 1
            in_out[d][0] += 1
        # Airports that we have no route to yet, a.k.a: unreachable.
        missing = set(airports)
        # We need to visit the starting airport.
        missing.remove(startingAirport)
        stack = [startingAirport]
        # We also need to visit any airports that do not currently have
        # any incoming flights, that means we need to create a flight to
        # them, lets visit them from the starting airport directly, that
        # way we can mark any airport that we can reach from any of them
        # as reachable as well.
        for airport in airports:
            incoming, _ = in_out[airport]
            if not incoming and airport != startingAirport:
                stack.append(airport)
                missing.remove(airport)
                extra_flights += 1
        # Create a list of airports sorted by their indegree in
        # ascending order, then their outdegree in descending order.
        sorted_airports = sorted(
            [(in_out[a][0], -in_out[a][1], a) for a in missing]
        )
        # While we have not yet visited all airports.
        while missing:
            # If we have any airports to visit in the stack.
            if stack:
                source = stack.pop()
                for nei in adj[source]:
                    # We can visit this airport with the existing
                    # flights.
                    if nei in missing:
                        missing.remove(nei)
                        stack.append(nei)
            # If we have exhausted the list of airports that we can
            # reach, we need to create a new flight.
            else:
                extra_flights += 1
                # Pick an airport within the ones with the lowest
                # indegree.
                for _, _, a in sorted_airports:
                    if a not in missing:
                        continue
                    # a is the airport that we haven't visited with the
                    # lowest indegree and the highest outdegree.
                    stack.append(a)
                    missing.remove(a)
                    break
        return extra_flights


def test():
    executors = [
        Solution,
        DoNotUse,
    ]
    tests = [
        [
            [
                "BGI",
                "CDG",
                "DEL",
                "DOH",
                "DSM",
                "EWR",
                "EYW",
                "HND",
                "ICN",
                "JFK",
                "LGA",
                "LHR",
                "ORD",
                "SAN",
                "SFO",
                "SIN",
                "TLV",
                "BUD",
            ],
            [],
            "LGA",
            17,
        ],
        [
            [
                "BGI",
                "CDG",
                "DEL",
                "DOH",
                "DSM",
                "EWR",
                "EYW",
                "HND",
                "ICN",
                "JFK",
                "LGA",
                "LHR",
                "ORD",
                "SAN",
                "SFO",
                "SIN",
                "TLV",
                "BUD",
            ],
            [
                ["DSM", "ORD"],
                ["ORD", "BGI"],
                ["BGI", "LGA"],
                ["SIN", "CDG"],
                ["CDG", "SIN"],
                ["CDG", "BUD"],
                ["DEL", "DOH"],
                ["DEL", "CDG"],
                ["TLV", "DEL"],
                ["EWR", "HND"],
                ["HND", "ICN"],
                ["HND", "JFK"],
                ["ICN", "JFK"],
                ["JFK", "LGA"],
                ["EYW", "LHR"],
                ["LHR", "SFO"],
                ["SFO", "SAN"],
                ["SFO", "DSM"],
                ["SAN", "EYW"],
            ],
            "LGA",
            3,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.airportConnections(t[0], t[1], t[2])
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
