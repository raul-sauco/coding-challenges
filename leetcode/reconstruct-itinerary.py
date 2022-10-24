# 332. Reconstruct Itinerary
# 🔴 Hard
#
# https://leetcode.com/problems/reconstruct-itinerary/
#
# Tags: Depth-First Search - Graph - Eulerian Circuit

import timeit
from collections import defaultdict
from typing import List


# Create a dictionary of source: sorted_destinations, starting from JFK
# try visiting the possible destinations in lexicographical order until
# an itinerary that visits all the edges, or uses all the given tickets,
# is found, when we find that itinerary, return it. Anytime we arrive
# at a dead-end on the branch that we are exploring, we backtrack to
# the latest point where we made a decision and choose the next option
# until all the options on that branch have been exhausted, then we try
# another branch from higher in the recursion tree.
#
# Time complexity: O(v*e) - At most we will explore the combinations of
# v vertex and e edges.
# Space complexity: O(v+e) - The dictionary can grow to v+e size, the
# call stack will have a max height of v+1.
#
# Runtime: 81 ms, faster than 96.47%
# Memory Usage: 14.5 MB, less than 57.86%
class DFSBacktrack:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Use a dictionary of source: List[destinations]
        dest = defaultdict(list)
        for ticket in tickets:
            dest[ticket[0]].append(ticket[1])
        # Sort the destination list, this guarantees that we will always
        # return the valid itinerary with the smallest lexicographical
        # order.
        for key in dest.keys():
            dest[key].sort(reverse=True)
        # We need to start at JFK
        ans = ["JFK"]
        # Define a function that explores the possible destinations from
        # a given point.
        def bt() -> bool:
            # Save all the remaining destinations and the origin.
            possible_destinations = dest[ans[-1]]
            origin = ans[-1]
            # If we don't have any destinations left from this location.
            if not possible_destinations:
                return len(ans) == len(tickets) + 1
            for i in range(len(possible_destinations) - 1, -1, -1):
                # Modify the global state to use this destination.
                ans.append(possible_destinations[i])
                dest_copy = possible_destinations.copy()
                del dest_copy[i]
                dest[origin] = dest_copy
                # Return once the first viable itinerary has been found.
                if bt():
                    return True
                # Backtrack.
                dest[origin] = possible_destinations
                ans.pop()
            # If none of the answers matched return False.
            return False

        # Initial call.
        bt()
        # We will have an answer once we get here.
        return ans


# TODO Check the Eulerian circuit version that constructs the path on
# reverse.


def test():
    executors = [
        DFSBacktrack,
    ]
    tests = [
        [
            [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
            ["JFK", "NRT", "JFK", "KUL"],
        ],
        [
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        ],
        [
            [
                ["JFK", "SFO"],
                ["JFK", "ATL"],
                ["SFO", "ATL"],
                ["ATL", "JFK"],
                ["ATL", "SFO"],
            ],
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findItinerary(t[0])
                exp = t[1]
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
