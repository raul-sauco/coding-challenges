import unittest
from collections import deque

from data import TreeNode


# Given the head of a complete tree and a value, determine if the value is in the tree.
def hasValue(head: TreeNode, key: int) -> bool:
    stack = deque()
    stack.append(key)
    node = key >> 1
    while node > 1:
        stack.append(node)
        node = node >> 1
    current_node = head
    while stack:
        current = stack.pop()
        if current % 2 == 1:
            if current_node.right:
                current_node = current_node.right
            else:
                return False
        else:
            if current_node.left:
                current_node = current_node.left
            else:
                return False
    return True


def test():
    node756 = TreeNode(val=756)
    node378 = TreeNode(val=378, left=node756)
    node189 = TreeNode(val=189, left=node378)
    node94 = TreeNode(val=94, right=node189)
    node47 = TreeNode(val=47, left=node94)
    node23 = TreeNode(val=23, right=node47)
    node11 = TreeNode(val=11, right=node23)
    node5 = TreeNode(val=5, right=node11)
    node3 = TreeNode(val=3)
    node2 = TreeNode(val=2, right=node5)
    node1 = TreeNode(val=1, left=node2, right=node3)

    result = hasValue(node1, 756)
    assert result, f'{result} != True'

    result = hasValue(node1, 780)
    assert not result, f'{result} != False'


test()
