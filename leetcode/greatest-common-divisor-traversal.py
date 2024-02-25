# 2709. Greatest Common Divisor Traversal
# 🔴 Hard
#
# https://leetcode.com/problems/greatest-common-divisor-traversal/
#
# Tags: Array - Math - Union Find - Number Theory

import timeit
from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find_parent(self, a):
        if a != self.parents[a]:
            self.parents[a] = self.find_parent(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        pa, pb = self.find_parent(a), self.find_parent(b)
        if pa == pb:
            return
        if self.rank[pb] > self.rank[pa]:
            return self.union(b, a)
        self.parents[pb] = pa
        self.rank[pa] += self.rank[pb]
        self.components -= 1


# A really interesting problem, combining elements of graphs with some math. The numbers in
# the input can be seen as nodes in a graph, the edges can be computed factorizing the
# numbers, any two values that share a common factor are connected, the graph is undirected,
# the problem asks us to determine if the graph is connected. The simplest way to compute the
# number of disjoint components in a graph is to use Union Find, if the graph has one
# component, it is connected, otherwise it isn't. We can initialize a union find structure,
# and a hashmap that keeps factors as keys and the index of a representative of that factor
# groups as the value, for each factor in a number, if we have seen that factor previously,
# we union the current index to that set, if we haven't we initialize a new set and use the
# current index as the representative. Since we know that the values are limited to 100000,
# we can optimize the computation of factors using an array of hardcoded primes, this array
# contains the 64 primes found between 2 and sqr(100000), any prime that is a factor of an
# input value we will obtain as the remainder of having removed all the prime factors up to,
# and including, 311. For example, the next prime 317, will need to be combined with a prime
# <= 311, because 317^2 = 100489.
#
# Time complexity: O(n) - Filtering duplicates is O(n), then iterating over the input is O(n)
# as well, because in the inner loop we iterate a fixed number of times, 64, calling the
# union operation in the union find structure is amortized O(1).
# Space complexity: O(n) - The union-find structure, and the representatives hashmap both can
# grow to size n. The representatives hashmap is more likely going to be closer to size 64,
# but that is not guaranteed, for example, every element in the input could be a prime > 311,
# each would result in an entry in the representatives set.
#
# Runtime 749 ms Beats 87.50%
# Memory 32.75 MB Beats 28.13%
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        # Remove duplicates
        nums = list(set(nums))
        n = len(nums)
        uf = UnionFind(n)
        # fmt: off
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
            67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
            139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
            211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
            281, 283, 293, 307, 311,
        ]
        # fmt: on

        # A hashmap, given a factor, points to the index of a value in that component.
        representatives = defaultdict(int)

        for idx, num in enumerate(nums):
            val = num
            if val == 1:
                return False
            for prime in primes:
                if val % prime == 0:
                    if (i := representatives.get(prime, -1)) != -1:
                        uf.union(idx, i)
                    else:
                        representatives[prime] = idx
                while val % prime == 0:
                    val //= prime
            if val != 1:
                # The remainder is also a prime, it could be a factor in some other value.
                if (i := representatives.get(val, -1)) != -1:
                    uf.union(idx, i)
                else:
                    representatives[val] = idx

        return uf.components == 1


def test():
    executors = [Solution]
    tests = [
        ([1], True),
        ([1, 1], False),
        ([2, 3, 6], True),
        ([3, 9, 5], False),
        ([4, 3, 12, 8], True),
        ([10007, 20014], True),
        (
            [
                42,
                40,
                45,
                42,
                50,
                33,
                30,
                45,
                33,
                45,
                30,
                36,
                44,
                1,
                21,
                10,
                40,
                42,
                42,
            ],
            False,
        ),
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.canTraverseAllPairs(t[0])
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
