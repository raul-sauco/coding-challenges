# 146. LRU Cache
# 🟠 Medium
#
# https://leetcode.com/problems/lru-cache/
#
# Tags: Hash Table - Linked List - Design - Doubly-Linked List

from __future__ import annotations

import timeit
from collections import OrderedDict

# Useful to watch the current state of the cache in the watch tab of the
# debugger using the watch expression `serializeLinkedList(self.lru)`
from data import serializeLinkedList


# A doubly linked list node.
class DListNode:
    def __init__(
        self,
        prev: DListNode = None,
        next: DListNode = None,
        val: int = 0,
        key: int = 0,
    ):
        self.prev = prev
        self.next = next
        self.val = val
        self.key = key


# Design the LRUCache using a dictionary to have O(1) access to any
# element in the cache via the key, and a doubly linked list, to also
# have O(1) access to both ends of the list, the LRU and MRU elements.
# The dictionary uses integers as keys and doubly linked list nodes as
# values. The nodes store their value, the key, to have O(1) removal of
# the LRU, and pointers to the next and previous siblings.
#
# Time complexity: O(1) - For init, get and put methods.
# Space complexity: O(n) - Both the list and the cache will grow
# linearly with the size of the input.
#
# Runtime: 959 ms, faster than 83.51%
# Memory Usage: 75.8 MB, less than 42.75%
class LRUCache:
    def __init__(self, capacity: int):
        # Initialize the class attributes.
        self.capacity = capacity
        # A dictionary of key => ListNode.
        self.cache = {}
        # The least recently used key.
        self.lru = None
        # The most recently used key.
        self.mru = None

    def get(self, key: int) -> int:
        if key in self.cache:
            node: DListNode = self.cache[key]
            self.touch(node)
            return node.val
        else:
            # Return -1 for key not found.
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node: DListNode = self.cache[key]
            # Update the lru references.
            node.val = value
            self.touch(node)
        # If the key does not exist, add it, it may be necessary to
        # remove the lru node.
        else:
            if len(self.cache) == self.capacity:
                # Evict lru key.
                del self.cache[self.lru.key]
                if self.capacity == 1:
                    self.lru = None
                    self.mru = None
                else:
                    self.lru = self.lru.next
                    self.lru.prev = None
            # Now we are guaranteed to have space for one more node.
            node = DListNode(prev=self.mru, next=None, val=value, key=key)
            self.mru = node
            self.cache[key] = node
            # If this is the only node in the cache, it is also the lru.
            if len(self.cache) == 1:
                self.lru = node
            # If there are more nodes, update its prev to link to it.
            else:
                node.prev.next = node

    def touch(self, node: DListNode) -> None:
        # Update the lru references if the currently accessed node
        # is not the most recently used node already.
        # If node already is the most recently used node do nothing.
        if self.mru == node:
            return
        if self.lru == node:
            # Update end of the list removing this node.
            node.next.prev = None
            self.lru = node.next
        else:
            # Remove this node from the list updating its siblings
            # pointers.
            node.next.prev = node.prev
            node.prev.next = node.next
        # Update start of the list adding this node as the new mru.
        node.prev = self.mru
        self.mru.next = node
        self.mru = node


# Use collections.OrderedDictionary to implement the LRUCache, we only
# need to worry about checking the size and moving the accessed element
# to the MRU position, the rest of the operations are supported by the
# OrderedDictionary itself.
#
# Time complexity: O(1) - This solution uses the OrderedDictionary
# methods `move_to_end` and `popitem`, both of them are O(1).
# Space complexity: O(n) - The OrderedDictionary will grow to the same
# size as the input.
#
# Runtime: 1419 ms, faster than 40.37%
# Memory Usage: 74.6 MB, less than 94.63%
class OrDictLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def test():
    executors = [
        LRUCache,
        OrDictLRUCache,
    ]
    tests = [
        # Edge case with capacity 1. Lru and mru are always the same.
        [
            [
                "LRUCache",
                "put",
                "put",
                "get",
                "get",
                "put",
                "get",
                "put",
                "get",
                "get",
                "get",
            ],
            [
                [1],
                [1, 1],
                [2, 2],
                [1],
                [2],
                [3, 3],
                [2],
                [4, 4],
                [1],
                [3],
                [4],
            ],
            [None, None, None, -1, 2, None, -1, None, -1, -1, 4],
        ],
        # Regular case with capacity > 1.
        [
            [
                "LRUCache",
                "put",
                "put",
                "get",
                "put",
                "get",
                "put",
                "get",
                "get",
                "get",
            ],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ],
        [
            [
                "LRUCache",
                "put",
                "put",
                "get",
                "put",
                "get",
                "put",
                "get",
                "get",
                "get",
            ],
            [[2], [1, 0], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
            [None, None, None, 0, None, -1, None, -1, 3, 4],
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
