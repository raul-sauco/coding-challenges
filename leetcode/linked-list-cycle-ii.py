# 142. Linked List Cycle II
# 🟠 Medium
#
# https://leetcode.com/problems/linked-list-cycle-ii/
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
# Runtime 50 ms Beats 72.17%
# Memory 17.2 MB Beats 90.55%
class Floyd:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        # If the loop exits and the pointers do not point to the same
        # node, there is no cycle.
        else:
            return None
        fast = head
        while fast != slow:
            slow, fast = slow.next, fast.next
        return fast


# If the list nodes are hashable, or if they have unique values that we
# can hash, we can use a set, or a hashmap of value: node, to add
# nodes to, if we see a node that is already in the hash set, we can
# return it because that is the start of the cycle.
#
# Time complexity: O(n) - Linear time if we consider hashing O(1).
# Space complexity: O(n) - The set can grow to size n.
#
# Runtime 55 ms Beats 52.57%
# Memory 17.9 MB Beats 21.35%
class Set:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        seen = {current}
        while current.next:
            current = current.next
            if current in seen:
                return current
            seen.add(current)
        return None


print(f"\033[93m» This file does not have any tests\033[0m")
