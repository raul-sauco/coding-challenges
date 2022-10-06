# 981. Time Based Key-Value Store
# 🟠 Medium
#
# https://leetcode.com/problems/time-based-key-value-store/
#
# Tags: Hash Table - String - Binary Search - Design

import timeit
from bisect import bisect_right
from collections import defaultdict


# The store will consist of a hashmap with strings as keys and arrays
# as values, since we are guaranteed to have strictly increasing
# timestamps, on set we can append the given timestamp and value to the
# given key's list, that will result in a list of values ordered by
# increasing timestamp. This sorted property lets us use binary search
# on the get method to obtain O(log(e)) time complexity, where e is the
# number of entries for the given key. This can lead to a worst time of
# O(log(n)) if all the values are under the same key.
#
# Space complexity: O(n) - With n the number of set calls, since we are
# storing all the elements given.
#
# Runtime: 797 ms, faster than 91.29%
# Memory Usage: 72.1 MB, less than 38.03%
class TimeMap:
    def __init__(self):
        # Initialize a dictionary of lists indexed by key.
        self.d = defaultdict(list)

    # O(1) - find the list by key and insert (amortized O(1) for insert)
    def set(self, key: str, value: str, timestamp: int) -> None:
        # Timestamps are guaranteed to be increasing, insert by key,
        # this will give us a list of tuple entries e in which e[0] is
        # the timestamp and e[1] is the value set at that timestamp.
        self.d[key].append((timestamp, value))

    # O(log(e)) - e is the number of items for the given key.
    def get(self, key: str, timestamp: int) -> str:
        # If key is in self.d it will have at least one element
        if key not in self.d or timestamp < self.d[key][0][0]:
            return ""
        values = self.d[key]
        l, r = 0, len(values)
        # Binary search the first value greater than this timestamp.
        while l < r:
            mid = (l + r) // 2
            if values[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid
        return values[l - 1][1]


# Same logic as the previous solution but use the built-in bisect_right
# function to find the insertion point.
#
# Space complexity: O(n) - With n the number of set calls, since we are
# storing all the elements given.
#
# Runtime: 1348 ms, faster than 49.60%
# Memory Usage: 70.7 MB, less than 86.55%
class TimeMapBisect:
    def __init__(self):
        # Initialize a dictionary of lists indexed by key.
        self.d = defaultdict(list)

    # O(1) - find the list by key and insert (amortized O(1) for insert)
    def set(self, key: str, value: str, timestamp: int) -> None:
        # Timestamps are guaranteed to be increasing, insert by key,
        # this will give us a list of tuple entries e in which e[0] is
        # the timestamp and e[1] is the value set at that timestamp.
        self.d[key].append((timestamp, value))

    # O(log(e)) - e is the number of items for the given key.
    def get(self, key: str, timestamp: int) -> str:
        values = self.d[key]
        if not values:
            return ""
        # Find the first index right of the value.
        idx = bisect_right(values, timestamp, key=lambda i: i[0])
        if not idx:
            return ""
        return values[idx - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


def test():
    executors = [
        TimeMap,
        TimeMapBisect,
    ]
    tests = [
        [
            ["TimeMap", "set", "get", "get", "set", "get", "get"],
            [
                [],
                ["foo", "bar", 1],
                ["foo", 1],
                ["foo", 3],
                ["foo", "bar2", 4],
                ["foo", 4],
                ["foo", 5],
            ],
            [None, None, "bar", "bar", None, "bar2", "bar2"],
        ],
        [
            [
                "TimeMap",
                "set",
                "get",
                "get",
                "set",
                "get",
                "get",
                "get",
                "set",
                "set",
                "get",
                "get",
                "get",
                "get",
            ],
            [
                [],
                ["foo", "bar", 4],
                ["foo", 4],
                ["foo", 3],
                ["foo", "baz", 20],
                ["foo", 4],
                ["foo", 20],
                ["foo", 21],
                ["foo", "bat", 21],
                ["foo", "bao", 22],
                ["foo", 21],
                ["foo", 22],
                ["foo", 19],
                ["foz", 40],
            ],
            [
                None,  # TimeMap()
                None,  # set("foo", "bar", 4)
                "bar",
                "",
                None,  # set("foo", "baz", 20)
                "bar",
                "baz",
                "baz",
                None,  # set("foo", "bat", 21)
                None,  # set("foo", "bao", 22)
                "bat",
                "bao",
                "bar",
                "",
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                # The capacity comes wrapped in an array, unwrap it.
                sol = executor()
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    if call == "get":
                        result = getattr(sol, call)(t[1][i][0], t[1][i][1])
                    else:
                        result = getattr(sol, call)(
                            t[1][i][0], t[1][i][1], t[1][i][2]
                        )
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
