# Count groups of friends.
#
# position[i][j] - Represents that user i has gifted user j and it is
# therefore in their group of relations. Find how many groups of related
# friends are in the matrix.
#
# Tags: Graph - DFS - BFS

import timeit
from collections import deque


# Iterate over the rows, for each row, check if we have added it to a
# row before, if we haven't, create a new row for it, then process all
# other users related to this one using BFS. It could also be DFS.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(n) - The set of seen. The queue could also grow
# to O(n) if, for example, every user was directly related to the first
# one.
class Solution:
    def countGroups(self, related):
        groups = 0
        # Create a set with all the people that we have put
        # in a group already.
        seen = set()
        # Iterate over rows that we haven't placed in a group yet.
        for row_idx in range(len(related)):
            # row_idx is also the user id.
            if row_idx in seen:
                # If we have placed this user in a group, skip it.
                continue
            # Else this user is the root of a new group.
            groups += 1
            current = row_idx
            # Touch all users related to this one using BFS.
            # Use a deque for BFS.
            q = deque()
            while current != None:
                seen.add(current)
                for col_idx in range(len(related[0])):
                    # If this users are related.
                    if (
                        col_idx not in seen
                        and current != col_idx
                        and related[current][col_idx] == "1"
                    ):
                        q.append(col_idx)

                # Process the next user.
                current = q.popleft() if q else None

        return groups


def test():
    executors = [Solution]
    tests = [
        [["1"], 1],
        [["100", "010", "001"], 3],
        [["1100", "1110", "0111", "0001"], 1],
        [["1100", "1110", "0110", "0001"], 2],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.countGroups(t[0])
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
