# Merging Linked Lists
# 🟠 Medium
#
# https://www.algoexpert.io/questions/merging-linked-lists
#
# Tags: Linked List

import timeit


# Count the number of nodes on both lists, then skip the difference in
# number of nodes on the longest list and start iterating them at the
# same time, if the lists merge at some point, their tails will be the
# same, if we arrive at the same node at some point, that is the
# intersection, if we don't, the lists do not intersect.
#
# Time complexity: O(n) - Where n is the number of nodes in both lists.
# Space complexity: O(1) - Extra constant memory used.
class Solution:
    def mergingLinkedLists(self, a, b):
        # Define a nested function that returns the length of a linked
        # list given its head.
        def getLength(linkedList) -> int:
            size = 0
            current = linkedList
            while current:
                size += 1
                current = current.next
            return size

        # Compute the length of both lists.
        len_a, len_b = getLength(a), getLength(b)
        # Make sure list one is the longest one.
        if len_a < len_b:
            len_a, len_b, a, b = len_b, len_a, b, a
        difference = len_a - len_b
        # Skip until we have the same number of remaining nodes.
        while difference:
            a = a.next
            difference -= 1
        # Travel both lists simultaneously.
        while a:
            if a is b:
                return a
            a, b = a.next, b.next
        return None


def test():
    executors = [Solution]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.mergingLinkedLists(t[0], t[1])
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
