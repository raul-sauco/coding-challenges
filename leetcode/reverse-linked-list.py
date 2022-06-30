# https://leetcode.com/problems/reverse-linked-list/


from typing import List, Optional
from data import ListNode


# Runtime: 42 ms, faster than 81.83% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 55.68 % of Python3 online submissions for Reverse Linked List.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        current = head
        next = current.next
        while next:
            prev = current
            current = next
            next = current.next
            current.next = prev
        head.next = None
        return current


def linkedListToArray(result: List[int], node: ListNode) -> List[int]:
    result.append(node.val)
    if node.next:
        return linkedListToArray(result, node.next)
    else:
        return result


def test():
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    sol = Solution()
    result = linkedListToArray([], sol.reverseList(node1))
    expected = [5, 4, 3, 2, 1]
    assert result == expected, f'{result} != {expected}'
    assert sol.reverseList(None) == None


test()
