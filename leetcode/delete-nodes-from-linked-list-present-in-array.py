# 3217. Delete Nodes From Linked List Present in Array
# 🟠 Medium
#
# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
#
# Tags: Array - Hash Table - Linked List

import timeit
from typing import List, Optional

from utils.linked_list import LinkedList, ListNode


# Convert the nums list into a hash set, create a dummy node to point to
# the head of the result linked list. Iterate over the list nodes, for
# each, while the next node's value is in the hash set, cut it out.
#
# Time complexity: O(n) - We iterate the entire linked list.
# Space complexity: O(m) - The extra hash set with the nums.
#
# Runtime 733 ms Beats 37%
# Memory 54 MB Beats 81%
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        nums = {num for num in nums}
        dummy = ListNode(0, head)
        cur = dummy
        while cur:
            while cur.next and cur.next.val in nums:
                cur.next = cur.next.next
            cur = cur.next
        return dummy.next


def test():
    executors = [Solution]
    tests = [
        [[1, 2, 3], [1, 2, 3, 4, 5], [4, 5]],
        [[1], [1, 2, 1, 2, 1, 2], [2, 2, 2]],
        [[5], [1, 2, 3, 4], [1, 2, 3, 4]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                head = LinkedList.fromList(t[1]).head
                result_head = sol.modifiedList(t[0], head)
                result = LinkedList(result_head).toList()
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
