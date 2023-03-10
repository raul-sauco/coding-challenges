# 382. Linked List Random Node
# 🟠 Medium
#
# https://leetcode.com/problems/linked-list-random-node/
#
# Tags: Linked List - Design

import random
import timeit
from typing import Optional

from utils.linked_list import ListNode


# Simple solution that uses extra memory. Iterate over the input linked
# list nodes and store them in an array then pick random elements from
# the array in O(1) when needed.
#
# Time complexity: O(n) - Init iterates over the entire linked list,
# then O(1) for getRandom.
# Space complexity: O(n) - We use an array of size n of extra memory.
#
# Runtime 60 ms Beats 98.51%
# Memory 17.2 MB Beats 97.21%
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Use reservoir sampling to lazily solve the problem, it only fetches
# nodes when required. For this problem it does not seem to make a lot
# of sense, but it is an interesting algorithm to be aware of. In this
# case, since we are iterating the entire list every time we call
# getRandom, it would make more sense to store the length of the list
# and then get a random value between 0..n and iterate up to that node
# to return its value.
#
# Time complexity: O(n) - O(1) for init, then get random iterates over
# the entire list every time it is called.
# Space complexity: O(1) - We use constant extra memory.
#
# Runtime 83 ms Beats 51.6%
# Memory 17.2 MB Beats 96.92%
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # We have a reservoir of size 1.
        size, candidate, node = 1, 0, self.head
        # Iterate over all nodes O(n)
        while node:
            if random.random() < 1 / size:
                candidate = node.val
            node = node.next
            size += 1
        return candidate


def test():
    executors = [Solution]
    tests = []
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.methodCall(t[0])
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
