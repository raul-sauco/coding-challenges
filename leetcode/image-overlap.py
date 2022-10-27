# 835. Image Overlap
# 🟠 Medium
#
# https://leetcode.com/problems/image-overlap/
#
# Tags: Array - Matrix

import timeit
from collections import Counter, defaultdict
from typing import List


# Store all positions that hold 1s in each matrix in a list. Then
# iterate over each combination of positions in the list computing the
# vector between them and adding 1 to the count of times that we have
# seen the given vector. The solution to the problem will come from
# shifting the matrix using the most common vector and it will equal the
# number of positions in a and b that have that vector in common.
#
# Time complexity: O(n^4) - In the worst case each position in both
# matrixes would have a 1 O(n^2) and we would check each combination of
# them O((n^2)*(n^2)).
# Space complexity: O(n^2) - Either list and also the dictionary could
# grow to size n*n.
#
# Runtime: 938 ms, faster than 59.65%
# Memory Usage: 14.6 MB, less than 43.86%
class VectorCounts:
    def largestOverlap(
        self, img1: List[List[int]], img2: List[List[int]]
    ) -> int:
        # Store the length of both of the matrixes height and width.
        N = len(img1)
        # Store all positions that have a 1 in a and b.
        ones_in_a, ones_in_b = [], []
        for i in range(N):
            for j in range(N):
                if img1[i][j]:
                    ones_in_a.append((i, j))
                if img2[i][j]:
                    ones_in_b.append((i, j))
        # Store a dictionary of vectors pointing to the number of times
        # we have seen that exact vector between two ones.
        count = defaultdict(int)
        # Store the highest count of matching vectors seen so far.
        res = 0
        for a_cell in ones_in_a:
            for b_cell in ones_in_b:
                vector = (b_cell[0] - a_cell[0], b_cell[1] - a_cell[1])
                count[vector] += 1
                if count[vector] > res:
                    res = count[vector]
        return res


# There is an interesting solution that flattens the positions with ones
# in both matrixes into lists and then checks their difference, the
# concept is similar to the previous solution but I thought that it was
# interesting enough to add it here.
#
# The original post is at:
# https://leetcode.com/problems/image-overlap/discuss/130623/C%2B%2BJavaPython-Straight-Forward
#
# Time complexity: O(N^4) - The original post gives it as O(AB + N^2)
# with A and B the number of 1s in A and B, as the number of 1s grows in
# the matrixes, A*B approaches n^4.
# Space complexity: O(n^2) - The original post gives it as O(A+B) which
# becomes O(n^2) when the entire matrix is made of 1s.
#
# Runtime: 567 ms, faster than 86.55%
# Memory Usage: 14.4 MB, less than 64.33%
class FlattenMatrix:
    def largestOverlap(
        self, img1: List[List[int]], img2: List[List[int]]
    ) -> int:
        N = len(img1)
        NN = N * N
        la = [i // N * 100 + i % N for i in range(NN) if img1[i // N][i % N]]
        lb = [i // N * 100 + i % N for i in range(NN) if img2[i // N][i % N]]
        c = Counter(i - j for i in la for j in lb)
        return max(c.values() or [0])


def test():
    executors = [
        VectorCounts,
        FlattenMatrix,
    ]
    tests = [
        [[[0]], [[0]], 0],
        [[[1]], [[1]], 1],
        [
            [[1, 1, 0], [0, 1, 0], [0, 1, 0]],
            [[0, 0, 0], [0, 1, 1], [0, 0, 1]],
            3,
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.largestOverlap(t[0], t[1])
                exp = t[2]
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
