# 460. LFU Cache
# 🔴 Hard
#
# https://leetcode.com/problems/lfu-cache/
#
# Tags: Hash Table - Linked List - Design - Doubly-Linked List

from __future__ import annotations

import queue
import timeit
from collections import defaultdict
from typing import List, Optional


# A node of a doubly linked list with key, value and use count properties.
class LFUNode:
    def __init__(
        self,
        key: int,
        value: int,
        prev: Optional[LFUNode] = None,
        next: Optional[LFUNode] = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        self.use_count = 1

    def __repr__(self):
        return "LFUNode({}:{})".format(self.key, self.value)


# A doubly linked list that allows three operations, adding a node to
# the tail, removing a given node or popping the node at the head.
class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        return self.size

    def __repr__(self):
        return "DLL({})".format(self.toList())

    # Serialize this linked list to an list containing the values in each node.
    def toList(self) -> List:
        result = []
        current: LFUNode = self.head
        if current and current.next:
            cycle_detect = current.next.next
        else:
            cycle_detect = None
        while current:
            result.append(current.value)
            current = current.next
            if cycle_detect:
                if cycle_detect == current:
                    raise Exception("DoublyLinkedList has a cycle", result)
                if cycle_detect.next:
                    cycle_detect = cycle_detect.next.next
                else:
                    cycle_detect = None
        return result

    def append(self, node: LFUNode):
        if not self.size:
            self.head = self.tail = node
            self.size = 1
            return self.size
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.size += 1
        return self.size

    # Pop the node used least recently from this queue.
    def pop(self) -> LFUNode:
        if not self.size:
            raise Exception("Cannot pop from an empty list")
        node = self.head
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return node

    def remove(self, node) -> int:
        if not self.size:
            raise Exception("Cannot remove from an empty list")
        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            return 0
        prev, next = node.prev, node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if node is self.head:
            self.head = next
        if node is self.tail:
            self.tail = prev
        node.next, node.prev = None, None
        self.size -= 1
        return self.size


# A cache with a given capacity, when we try to insert a node and the
# cache is already full, it will evict the node that has seen the least
# amount of use, if several nodes have seen the same minimal amount of
# use, it will remove the least recently used.
#
# Runtime 917 ms Beats 68.13%
# Memory 78.4 MB Beats 49.14%
class LFUCache:
    # Initialize a cache with the given capacity.
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._min_freq = 0
        self._nodes = {}
        self._freqs = defaultdict(DoublyLinkedList)

    # Mark the given node as having seen one use, it could be a get or
    # an update put operation. O(1)
    def touch(self, node: LFUNode):
        uc = node.use_count
        f = self._freqs[uc]
        if not f.remove(node) and uc == self._min_freq:
            self._min_freq += 1
        node.use_count += 1
        self._freqs[uc + 1].append(node)

    # O(1) - If the node is found, return its value otherwise -1. If
    # the node exists, it will register its access in O(1).
    def get(self, key: int) -> int:
        if key not in self._nodes:
            return -1
        node: LFUNode = self._nodes[key]
        self.touch(node)
        return node.value

    # O(1) - If the key is not found in the cache, insert a new key,
    # value pair, if found, update its value and register the access.
    def put(self, key: int, value: int) -> None:
        # Base case, cache cannot hold any elements.
        if not self._capacity:
            return None
        node = LFUNode(key, value)
        # If the cache is empty just append this node.
        if not self._nodes:
            self._freqs[1].append(node)
            self._nodes[key] = node
            self._min_freq = 1
            return None
        # The key exists already.
        if key in self._nodes:
            node: LFUNode = self._nodes[key]
            node.value = value
            self.touch(node)
            return None
        # If the cache is full, pop one.
        if len(self._nodes) == self._capacity:
            nodeToRemove = self._freqs[self._min_freq].pop()
            del self._nodes[nodeToRemove.key]
            del nodeToRemove
        self._freqs[1].append(node)
        self._nodes[key] = node
        # This recently inserted node has a frequency of 1.
        self._min_freq = 1


def test():
    executors = [LFUCache]
    tests = [
        [
            [
                "LFUCache",
                "put",
                "put",
                "get",
                "put",
                "get",
                "get",
                "put",
                "get",
                "get",
                "get",
            ],
            [
                [2],
                [1, 1],
                [2, 2],
                [1],
                [3, 3],
                [2],
                [3],
                [4, 4],
                [1],
                [3],
                [4],
            ],
            [None, None, None, 1, None, -1, 3, None, -1, 3, 4],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                # The capacity comes wrapped in an array, unwrap it.
                sol = executor(t[1][0][0])
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    if call == "get":
                        result = getattr(sol, call)(t[1][i][0])
                    else:
                        result = getattr(sol, call)(t[1][i][0], t[1][i][1])
                    exp = t[2][i]
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
