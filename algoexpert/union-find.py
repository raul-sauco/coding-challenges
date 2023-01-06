# Union Find
# 🟠 Medium
#
# https://www.algoexpert.io/questions/union-find
#
# Tags: Famous Algorithms - Union Find

import timeit


# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.rank = {}

    # Time complexity: O(1)
    # Space complexity: # O(α(n)), approximately O(1) time | O(α(n)), approximately O(1) space - where n is the total number of values
    def createSet(self, value):
        self.parents[value] = value
        self.rank[value] = 1

    # Time complexity: O(α(n)) - Approx O(1) because of path compression.
    # Space complexity: O(1)
    def find(self, value):
        if value not in self.parents:
            return None
        if self.parents[value] == value:
            return self.parents[value]
        # Use path compression.
        self.parents[value] = self.find(self.parents[value])
        return self.parents[value]

    # Time complexity: O(α(n)) - Approx O(1) because of path compression.
    # Space complexity: O(1)
    def union(self, valueOne, valueTwo):
        parent_a, parent_b = self.find(valueOne), self.find(valueTwo)
        if parent_a is None or parent_b is None or parent_a == parent_b:
            return
        # Choose the parent with the highest rank to merge under.
        if self.rank[parent_a] < self.rank[parent_b]:
            parent_a, parent_b = parent_b, parent_a
        self.parents[parent_b] = parent_a
        self.rank[parent_a] += self.rank[parent_b]


def test():
    executors = [UnionFind]
    tests = []
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
