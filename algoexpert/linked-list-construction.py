# Linked List Construction
# 🟠 Medium
#
# https://www.algoexpert.io/questions/linked-list-construction
#
# Tags: Linked List - Design

import timeit


# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# A doubly linked list class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Time complexity: O(1)
    # Space complexity: O(1)
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # Time complexity: O(1)
    # Space complexity: O(1)
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # Time complexity: O(1)
    # Space complexity: O(1)
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev:
            node.prev.next = nodeToInsert
        else:
            self.head = nodeToInsert
        node.prev = nodeToInsert
        # self.printAsList()

    # Time complexity: O(1)
    # Space complexity: O(1)
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next:
            node.next.prev = nodeToInsert
        else:
            self.tail = nodeToInsert
        node.next = nodeToInsert

    # Time complexity: O(k) - We need to iterate over k positions to
    # find the node at that position, then we use O(1) methods.
    # Space complexity: O(1)
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # Time complexity: O(n) - We need to iterate over n nodes to
    # find the node with the given value, n could be the entire linked
    # list, then we use O(1) methods.
    # Space complexity: O(1)
    def removeNodesWithValue(self, value):
        # print(f"» Removing node with value {value}")
        node = self.head
        while node:
            current = node
            node = node.next
            if current.value == value:
                self.remove(current)

    # Time complexity: O(1)
    # Space complexity: O(1)
    def remove(self, node):
        # print(f"» Removing node {node.value}")
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    # Time complexity: O(n) - We need to iterate over n nodes to
    # find the node with the given value, n could be the entire linked
    # list, then we use O(1) methods.
    # Space complexity: O(1)
    def containsNodeWithValue(self, value):
        # print(f"» Checking contains node with value {value}")
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    # Time complexity: O(n) - We iterate the entire list.
    # Space complexity: O(n) - We store the values in a list that later
    # we join and print.
    def printAsList(self):
        res = []
        current = self.head
        while current:
            res.append(str(current.value))
            current = current.next
        print("  " + " » ".join(res))


def test():
    executors = [DoublyLinkedList]
    tests = []  # TODO add tests.
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
