# Find Loop
# 🔴 Hard
#
# https://www.algoexpert.io/questions/find-loop
#
# Tags: Linked List - Cycle Detection

import timeit


# Use Floyd's Tortoise and Hare cycle detection algorithm. The tortoise
# and the hare start at the same time and move at different speeds until
# they intersect. Once the two pointers intersect, make the tortoise
# point to the head of the list and slow the hare to the same speed as
# the tortoise, keep iterating until they intersect again, that
# second intersection point is the first node in the cycle.
#
# Time complexity: O(n) - We will visit the nodes a linear number of
# times.
# Space complexity: O(1) - Constant extra memory used.
class Solution:
    def findLoop(self, head):
        tortoise, hare = head.next, head.next.next
        # First loop until they intersect.
        while tortoise is not hare:
            tortoise = tortoise.next
            hare = hare.next.next
        # Reset the tortoise to head, they move at the same speed.
        tortoise = head
        while tortoise is not hare:
            tortoise = tortoise.next
            hare = hare.next
        return tortoise


def test():
    executors = [Solution]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findLoop(t[0])
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
