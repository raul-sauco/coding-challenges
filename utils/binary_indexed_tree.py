from __future__ import annotations

from typing import List


# A Binary Indexed Tree, also called Fenwick Tree implementation.
#
# The binary indexed tree performs both insertion and range sum calculations in
# O(n*log(n)) time.
class BinaryIndexedTree:

    # Initialize a new instance of the BITree of the given size.
    # The sums array will be of size n + 1 because idx 0 is a dummy node that
    # acts as parent of all powers of 2.
    def __init__(self, size: int) -> None:
        self.sums = [0] * (size + 1)

    # Construct a binary indexed tree from a given list of values.
    def fromList(values: List[int]) -> BinaryIndexedTree:
        bit = BinaryIndexedTree(len(values))
        for i, val in enumerate(values):
            bit.update(i, val)
        return bit

    # Get the sums of all the list values from 0 to index. O(log(n)).
    def getSum(self, idx: int) -> int:
        # Start at idx + 1.
        idx += 1

        # Initialize the total at 0.
        total = 0

        # Iterate over all the parents of idx adding their content to the sum.
        while idx > 0:
            total += self.sums[idx]

            # Obtain the parent of the current index shifting the last 1 bit.
            # index = index - index & (-index)
            # For example, starting at 15:
            # 15: 1111
            # 14: 1110
            # 12: 1100
            #  8: 1000
            #  0
            idx -= idx & (-idx)

        return total

    # Get the sum of a range of values from start (inclusive) to end (exclusive).
    def getRangeSum(self, start: int, end: int) -> int:
        if not 0 <= start < end:
            return 0
        return self.getSum(end - 1) - self.getSum(start - 1)

    def update(self, idx: int, val: int) -> None:
        # Start at idx + 1.
        idx += 1

        # Visit all parents of index and add the given value to their current value. O(log(n)).
        while idx <= len(self.sums):
            self.sums[idx] += val

            # Obtain the parent of the current index shifting the last 1 bit.
            # index = index + index & (-index)
            # For example, starting at 1:
            #  1: 00001
            #  2: 00010
            #  4: 00100
            #  8: 01000
            # 16: 10000
            idx += idx & (-idx)


# https://en.wikipedia.org/wiki/Fenwick_tree
