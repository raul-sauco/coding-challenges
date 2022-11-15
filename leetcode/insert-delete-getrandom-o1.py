# 380. Insert Delete GetRandom O(1)
# 🟠 Medium
#
# https://leetcode.com/problems/insert-delete-getrandom-o1/
#
# Tags: Array - Hash Table - Math - Design - Randomized

import random
import timeit


# The naive O(n) for getRandom solution passes the tests.
#
# Runtime: 622 ms, faster than 78.94%
# Memory Usage: 61 MB, less than 93.94%
class RandomizedSetOn:
    def __init__(self):
        self.s = set()

    # O(1)
    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s.add(val)
        return True

    # O(1)
    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    # O(n) - The entire set gets converted to a tuple.
    def getRandom(self) -> int:
        if self.s:
            return random.choice(tuple(self.s))


# We can use a list to provide random access to elements by index and a
# hashmap of element value: list index to provide O(1) removals,
# insertion is O(1) for the hashmap and amortized O(1) for the list.
#
# Time complexity: O(1) - All methods.
# Space complexity: O(n) - We keep all elements in two data structures.
#
# Runtime: 1169 ms, faster than 34.30%
# Memory Usage: 61.2 MB, less than 85.69%
class RandomizedSetO1:
    def __init__(self):
        self.s = {}
        self.l = []

    # O(1)
    def insert(self, val: int) -> bool:
        # If the element is in the set, skip insertion.
        if val in self.s:
            return False
        # Append the element to the list and its index to the hashmap
        # indexed by value.
        self.l.append(val)
        self.s[val] = len(self.l) - 1
        return True

    # O(1)
    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        # If this element is the last element of the list, pop it.
        if self.s[val] == len(self.l) - 1:
            self.l.pop()
            self.s.pop(val)
        else:
            # If val is not the last element, move the last element to
            # its position. O(1).
            last, idx = self.l.pop(), self.s[val]
            self.l[idx], self.s[last] = last, idx
            self.s.pop(val)
        return True

    # O(1)
    def getRandom(self) -> int:
        return random.choice(self.l)


def test():
    executors = [
        RandomizedSetOn,
        RandomizedSetO1,
    ]
    tests = [
        [
            [
                "RandomizedSet",
                "insert",
                "remove",
                "insert",
                "getRandom",
                "remove",
                "insert",
                "getRandom",
            ],
            [[], [1], [2], [2], [], [1], [2], []],
            [None, True, False, True, 2, True, False, 2],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    if call == "getRandom":
                        # Skip testing get random.
                        result = getattr(sol, call)()
                    else:
                        argument = t[1][i][0]
                        result = getattr(sol, call)(argument)
                        exp = t[2][i]
                        assert result == exp, (
                            f"\033[93m» {result} <> {exp}\033[91m for"
                            + f" test {col}.{i} {call}({argument}) using "
                            + f"\033[1m{executor.__name__}"
                        )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
