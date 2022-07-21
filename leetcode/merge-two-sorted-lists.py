# https://leetcode.com/problems/merge-two-sorted-lists/


from typing import List, Optional

from helpers import BColors


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 40 ms, faster than 89.68% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14 MB, less than 32.07 % of Python3 online submissions for Merge Two Sorted Lists.
class Solution:
    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        head_pointer = temp = ListNode()
        while node1 != None and node2 != None:
            if node1.val < node2.val:
                temp.next = node1
                node1 = node1.next
            else:
                temp.next = node2
                node2 = node2.next
            temp = temp.next
        temp.next = node1 or node2
        return head_pointer.next

    # This has an error that leads to infinite recursion
    def mergeTwoListsRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


def linkedListToArray(result: List[int], node: ListNode) -> List[int]:
    result.append(node.val)
    if node.next:
        return linkedListToArray(result, node.next)
    else:
        return result


def test():
    # Test linkedListToArray
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    assert linkedListToArray([], node1) == [1, 2, 3, 4]
    assert linkedListToArray([], ListNode(0)) == [0]

    # Main tests
    sol = Solution()

    # Input: list1 = [1,2,4], list2 = [1,3,4]
    # Output: [1, 1, 2, 3, 4, 4]
    t_node_1_4 = ListNode(4)
    t_node_1_2 = ListNode(2, t_node_1_4)
    t_node_1_1 = ListNode(1, t_node_1_2)

    t_node_2_4 = ListNode(4)
    t_node_2_3 = ListNode(3, t_node_2_4)
    t_node_2_1 = ListNode(1, t_node_2_3)
    assert linkedListToArray([], sol.mergeTwoLists(
        t_node_1_1, t_node_2_1)) == [1, 1, 2, 3, 4, 4]

    # Test empties
    empty_node_1 = ListNode()
    empty_node_2 = ListNode()
    assert linkedListToArray([], sol.mergeTwoLists(
        empty_node_1, empty_node_2)) == [0, 0]
    assert sol.mergeTwoLists(None, None) == None

    empty_node_1 = ListNode()
    empty_node_2 = ListNode()
    assert linkedListToArray([], sol.mergeTwoLists(
        None, empty_node_2)) == [0], f'{linkedListToArray([], sol.mergeTwoLists( None, empty_node_2))} not equal to expected [0]'

    print(f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')


test()
