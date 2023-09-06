# 725. Split Linked List in Parts
# 🟠 Medium
#
# https://leetcode.com/problems/split-linked-list-in-parts/
#
# Tags: Linked List

import timeit
from typing import List, Optional

from utils.linked_list import ListNode


# Count the number of nodes in the list, then iterate over the nodes
# creating chunks of the required size, we will have n % k chunks of
# size n // k + 1 and the rest will be of size n // k, if there are
# less than k nodes, we will have some empty elements at the tail of the
# result array.
#
# Time complexity: O(max(n, k)) - We need to visit each list node, if
# there are less nodes than k, we still need to create an array of
# size k.
# Space complexity: O(k) - We create an array of size k.
#
# Runtime 46 ms Beats 56.31%
# Memory 16.59 MB Beats 97.75%
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        res = [None] * k
        i = 0
        while head:
            section_head = head
            section_size = (
                (length // k) if length % k == 0 else (length // k + 1)
            )
            length -= section_size
            prev = None
            for _ in range(section_size):
                prev, head = head, head.next
            prev.next = None
            res[i] = section_head
            i += 1
            k -= 1
        return res


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
