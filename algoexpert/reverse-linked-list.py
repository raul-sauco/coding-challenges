# Reverse Linked List
# 🔴 Hard
#
# https://www.algoexpert.io/questions/reverse-linked-list
#
# Tags: Linked List

import timeit

from utils.linked_list import LinkedList


# A simple solution that is a nice template to memorize and use on any
# list reversal problem.
#
# Time complexity: O(n) - We visit each node once.
# Space complexity: O(1) - We use constant memory.
class Solution:
    def reverseLinkedList(self, head):
        prev, current = None, head
        while current:
            current.next, current, prev = prev, current.next, current
        return prev


def test():
    executors = [Solution]
    tests = [
        [[], []],
        [[1, 2], [2, 1]],
        [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
        [[0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[0]).getHead()
                result = LinkedList(sol.reverseLinkedList(head)).toList()
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
