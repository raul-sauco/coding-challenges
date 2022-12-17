# BST Construction
# 🟠 Medium
#
# https://www.algoexpert.io/questions/bst-construction
#
# Tags: Binary Search Tree - Binary Tree - Design

import timeit
from collections import deque
from typing import List, Optional


# A Binary Search Tree implementation using nodes.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "BST({})".format(self.value)

    # Time: O(log(n)) best | O(n) worst.
    # Space: O(log(n)) best | O(n) worst.
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        # Do not edit the return statement of this method.
        return self

    # Time: O(log(n)) best | O(n) worst.
    # Space: O(log(n)) best | O(n) worst.
    def contains(self, value):
        if self.value == value:
            return True
        # Greater values should be to the right.
        if self.value < value:
            if self.right:
                return self.right.contains(value)
        # Smaller values should be to the left.
        elif self.left:
            return self.left.contains(value)
        return False

    # Time: O(log(n)) best | O(n) worst.
    # Space: O(log(n)) best | O(n) worst.
    def remove(self, value, parent=None):
        # The value to remove would be to the right of this node.
        if self.value < value:
            # Ignore values not found.
            if self.right:
                self.right.remove(value, self)
        # The value to remove would be to the left of this node.
        elif self.value > value:
            # Ignore values not found.
            if self.left:
                self.left.remove(value, self)
        # The value to remove matches this node's value.
        else:
            # Two children case.
            if self.left and self.right:
                # Update the value to the next greater or equal and
                # recursively remove that node.
                self.value = self.right.getMinValue()
                # Remove the node with the value that we are using as
                # the new value for this node.
                self.right.remove(self.value, self)
            # Handle the case when this node is the root node.
            elif not parent:
                if self.left or self.right:
                    node = self.left if self.left else self.right
                    self.value = node.value
                    self.left = node.left
                    self.right = node.right
                # No parent and no children, do nothing to this node.
            # This node is part of a subtree.
            elif parent.left == self:
                parent.left = self.left if self.left else self.right
            elif parent.right == self:
                parent.right = self.right if self.right else self.left
        # Do not edit the return statement of this method.
        return self

    def getMinValue(self) -> int:
        return self.left.getMinValue() if self.left else self.value

    # Serialize this binary tree to a list of integers.
    def toList(self) -> List[Optional[int]]:
        result = []
        if not self:
            return []
        queue = deque([self])
        # While we have elements and the current level is not all nulls
        while queue and set(queue) != {None}:
            # Process the next level
            for _ in range(len(queue)):
                current = queue.popleft()
                if not current:
                    result.append(None)
                else:
                    result.append(current.value)
                    queue.append(current.left)
                    queue.append(current.right)

        # Clean all trailing Nones from the result
        while result and result[-1] is None:
            result.pop()

        return result


# TODO: Add an iterative solution with O(1) memory complexity.


def bstFromList(values: List[int]) -> BST | None:
    if not values:
        return None
    bst = BST(values[0])
    for val in values[1:]:
        bst.insert(val)
    return bst


def test():
    start = timeit.default_timer()
    bst = bstFromList([10, 5, 15, 2, 5, 13, 22, 1, 14])
    exp = [10, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14]
    result = bst.toList()
    assert result == exp, f"\033[93m» {result} <> {exp}"
    bst.insert(12)
    exp = [10, 5, 15, 2, 5, 13, 22, 1, None, None, None, 12, 14]
    result = bst.toList()
    assert result == exp, f"\033[93m» {result} <> {exp}"
    bst.remove(10)
    exp = [12, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14]
    result = bst.toList()
    assert result == exp, f"\033[93m» {result} <> {exp}"
    assert bst.contains(15) is True, f"\033[93m» Should find node 15"
    assert bst.contains(51) is False, f"\033[93m» Should not find node 51"
    bst.insert(51)
    exp = [12, 5, 15, 2, 5, 13, 22, 1, None, None, None, None, 14, None, 51]
    result = bst.toList()
    assert result == exp, f"\033[93m» {result} <> {exp}"
    assert bst.contains(51) is True, f"\033[93m» Should find node 51"
    stop = timeit.default_timer()
    used = str(round(stop - start, 5))
    cols = "{0:20}{1:10}{2:10}"
    res = cols.format("BST", used, "seconds")
    print(f"\033[92m» {res}\033[0m")


test()
