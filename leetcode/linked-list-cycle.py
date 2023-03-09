# 141. Linked List Cycle
# 🟢 Easy
#
# https://leetcode.com/problems/linked-list-cycle/
#
# Tags: Hash Table - Linked List - Two Pointers


from typing import Optional

from utils.linked_list import ListNode


# Use the fast and slow pointer cycle detection algorithm.
# https://en.wikipedia.org/wiki/Cycle_detection
#
# Time complexity: O(n) - The complexity is linear over the number of
# nodes in the list.
# Space complexity: O(1) - We use constant extra space.
#
# Runtime 48 ms Beats 95.39%
# Memory 17.5 MB Beats 93.78%
class Floyd:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head.next, head.next.next
        while fast and fast.next and slow != fast:
            slow, fast = slow.next, fast.next.next
        return slow == fast


# If the list nodes are hashable, or if they have unique values that we
# can hash, we can use a set, or a hashmap of value: node, to add
# nodes to, if we see a node that is already in the hash set, we can
# return true because that is the start of the cycle.
#
# Time complexity: O(n) - Linear time if we consider hashing O(1).
# Space complexity: O(n) - The set can grow to size n.
#
# Runtime 45 ms Beats 98.30%
# Memory 17.9 MB Beats 8.15%
class Set:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        node, seen = head, set()
        while node.next and node not in seen:
            seen.add(node)
            node = node.next
        return node in seen


print(f"\033[93m» This file does not have any tests\033[0m")
