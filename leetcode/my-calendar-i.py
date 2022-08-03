# 729. My Calendar I
# 🟠 Medium
#
# https://leetcode.com/problems/my-calendar-i/
#
# Tags: Binary Search - Design - Segment Tree - Ordered Set

import timeit


# MyCalendar can be a BST with some customization. If we wanted it to be
# more performant, we could add self-balancing, but the simplest
# implementation it is enough to pass the tests.
#
# Time complexity: O(log(n)) for bookings and O(1) for init.
# Space complexity: O(n) - Each booking is stored as a node.
#
# Runtime: 429 ms, faster than 55.42%
# Memory Usage: 14.8 MB, less than 29.38%
class MyCalendar:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None

    def book(self, start: int, end: int) -> bool:
        # If this node does not have a value yet, add it.
        if not self.val:
            self.val = (start, end)
            return True

        # If there is any overlap, return False.
        if not (
            (start < self.val[0] and end <= self.val[0])
            or (start >= self.val[1] and end > self.val[1])
        ):
            return False

        # There is no overlap with this node, try to insert as a child.
        # The BST is ordered by start value.
        if start > self.val[0]:
            if not self.right:
                # There is no right child, create one.
                self.right = MyCalendar()
            return self.right.book(start, end)

        if start < self.val[0]:
            if not self.left:
                # There is no left child, create one.
                self.left = MyCalendar()
            return self.left.book(start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


def test():
    executors = [MyCalendar]
    tests = [
        [[[10, 20], [15, 25], [20, 30]], [True, False, True]],
        [
            [[1, 2], [2, 3], [4, 20], [6, 7], [3, 4], [-5, 1]],
            [True, True, True, False, True, True],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for i, t in enumerate(tests):
                sol = executor()
                for idx in range(len(t[0])):
                    s, e = t[0][idx]
                    result = sol.book(s, e)
                    exp = t[1][idx]
                    assert result == exp, (
                        f"\033[93m» {result} <> {exp}\033[91m for "
                        + f"test {i} using \033[1m{executor.__name__}"
                    )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
