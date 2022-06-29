# https://leetcode.com/problems/queue-reconstruction-by-height/

import timeit
from collections import defaultdict
from typing import List


# Intuition, if we only have people of the same or greater height in the array,
# and insert people of the same height starting by the lowest position, we can
# use the given index to insert them.
# Complexity is still high at O(n^2) because each insert costs O(n) on a list.
#
# Runtime: 166 ms, faster than 45.27% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.6 MB, less than 31.23 % of Python3 online submissions for Queue Reconstruction by Height.


class StartFromTaller:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Sort by height descending, then by position ascending
        people.sort(key=lambda person: (-person[0], person[1]))
        result = []
        for person in people:
            # Result only has people of >= height, insert at given position
            result.insert(person[1], person)
        return result

# Naive solution, we check all the positions before the insert for each insertion.

# Runtime: 707 ms, faster than 13.47% of Python3 online submissions for Queue Reconstruction by Height.
# Memory Usage: 14.5 MB, less than 31.23 % of Python3 online submissions for Queue Reconstruction by Height.


class Iterative:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        hs = defaultdict(list)
        result = [[float('inf'), float('inf')] for _ in range(len(people))]
        for person in people:
            hs[person[0]].append(person)

        for key in sorted(hs.keys()):
            for queuer in hs[key]:
                insert_at = queuer[1]
                # Check the positions up to, and including, the pos value
                i = 0
                while i < insert_at + 1:
                    if result[i][0] < queuer[0]:
                        # If the person at that position has >= height, move the insertion one position back
                        insert_at += 1
                    i += 1
                result[insert_at] = queuer

        return result


def test():
    executor = [
        {'executor': StartFromTaller, 'title': 'StartFromTaller', },
        {'executor': Iterative, 'title': 'Iterative', },
    ]
    tests = [
        [
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
        ],
        [
            [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]],
            [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]],
        ],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1'))):
            for t in tests:
                sol = e['executor']()
                result = sol.reconstructQueue(t[0])
                expected = t[1]
                assert result == expected, f'{result} != {expected} for {t[0]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
