# LRU Cache
# 🟣 Very Hard
#
# https://www.algoexpert.io/questions/lru-cache
#
# Tags: Linked List - Hash Map

import timeit

from utils.linked_list import LinkedList


# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.d = {}
        self.head = self.tail = None

    def insertKeyValuePair(self, key, value):
        # If the node exists already.
        if key in self.d:
            nodeToUpdate = self.d[key]
            nodeToUpdate.val = value
            self.touch(nodeToUpdate)
            return
        # This is a new insert.
        nodeToInsert = DLNode(key, value)
        if not self.head:
            self.head = self.tail = nodeToInsert
            self.d[nodeToInsert.key] = nodeToInsert
            return
        if len(self.d) == self.maxSize:
            nodeToRemove = self.tail
            if self.maxSize == 1:
                self.head = self.tail = nodeToInsert
            else:
                nodeToInsert.next = self.head
                self.head.prev = nodeToInsert
                self.head = nodeToInsert
                newTail = nodeToRemove.prev
                newTail.next = None
                self.tail = newTail
            self.d.pop(nodeToRemove.key)
        else:
            nodeToInsert.next = self.head
            self.head.prev = nodeToInsert
            self.head = nodeToInsert
        self.d[nodeToInsert.key] = nodeToInsert

    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.d:
            return None
        node = self.d[key]
        self.touch(node)
        return node.val

    def getMostRecentKey(self):
        # Write your code here.
        if self.head:
            return self.head.key
        return None

    def touch(self, node):
        if node is self.head:
            return
        p, n = node.prev, node.next
        p.next = n
        if n:
            n.prev = p
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node
        if self.tail is node:
            self.tail = p


class DLNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f"ListNode({self.key}:{self.val})"


def test():
    executors = [
        LRUCache,
    ]
    tests = [
        [
            [
                "LRUCache",
                "insertKeyValuePair",
                "insertKeyValuePair",
                "insertKeyValuePair",
                "getMostRecentKey",
                "getValueFromKey",
                "getMostRecentKey",
                "insertKeyValuePair",
                "getValueFromKey",
                "getMostRecentKey",
                "insertKeyValuePair",
                "getMostRecentKey",
                "getValueFromKey",
            ],
            [
                [3],
                ["b", 2],
                ["a", 1],
                ["c", 3],
                None,
                ["a"],
                None,
                ["d", 4],
                ["b"],
                None,
                ["a", 5],
                None,
                ["a"],
            ],
            [
                None,
                None,
                None,
                None,
                "c",
                1,
                "a",
                None,
                None,
                "d",
                None,
                "a",
                5,
            ],
        ],
        [
            [
                "LRUCache",
                "insertKeyValuePair",
                "insertKeyValuePair",
                "insertKeyValuePair",
                "insertKeyValuePair",
                "getValueFromKey",
                "getMostRecentKey",
                "insertKeyValuePair",
                "getValueFromKey",
                "getValueFromKey",
                "getValueFromKey",
                "insertKeyValuePair",
                "getValueFromKey",
                "getValueFromKey",
                "insertKeyValuePair",
                "getValueFromKey",
                "getValueFromKey",
                "getValueFromKey",
                "getValueFromKey",
                "getValueFromKey",
            ],
            [
                [4],
                ["a", 1],
                ["b", 2],
                ["c", 3],
                ["d", 4],
                ["a"],
                None,
                ["e", 5],
                ["a"],
                ["b"],
                ["c"],
                ["f", 5],
                ["c"],
                ["d"],
                ["g", 5],
                ["e"],
                ["a"],
                ["c"],
                ["f"],
                ["g"],
            ],
            [
                None,
                None,
                None,
                None,
                None,
                1,
                "a",
                None,
                1,
                None,
                3,
                None,
                3,
                None,
                None,
                None,
                1,
                3,
                5,
                5,
            ],
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
                    if call == "getValueFromKey":
                        result = getattr(sol, call)(t[1][i][0])
                    elif call == "getMostRecentKey":
                        result = getattr(sol, call)()
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
