# Merge Linked Lists
# 🔴 Hard
#
# https://www.algoexpert.io/questions/merge-linked-lists
#
# Tags: Linked List

import timeit

from utils.linked_list import LinkedList


# This is a template that can be used as the starting point of a
# solution with minimal changes.
class Solution:
    def mergeLinkedLists(headOne, headTwo):
        dummy = LinkedList(-1)
        current, a, b = dummy, headOne, headTwo
        # Add the next smallest value node.
        while a and b:
            if a.value < b.value:
                current.next = a
                a = a.next
            else:
                current.next = b
                b = b.next
            current = current.next
        # Consume the remaining of the lists.
        while a:
            current.next = a
            a = a.next
            current = current.next
        while b:
            current.next = b
            b = b.next
            current = current.next
        return dummy.next


def test():
    executors = [Solution]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.mergeLinkedLists(t[0], t[1])
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
