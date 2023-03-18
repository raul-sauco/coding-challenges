# 1472. Design Browser History
# 🟠 Medium
#
# https://leetcode.com/problems/design-browser-history/
#
# Tags: Array - Linked List - Stack - Design - Doubly-Linked List - Data Stream

import timeit


# We can optimize the previous solution and make all operations run in
# O(1) time if we use only one stack and keep both ints, one to know
# the index of the element that we are at currently, the other to
# determine how many steps forward we can move at this time.
#
# Time complexity: O(n) - Back and forward need to pop/push step
# elements between stacks, that is n where n is the value of steps.
# Space complexity: O(n) - Each call could result in one element added.
#
# Runtime 286 ms Beats 45.44%
# Memory 16.7 MB Beats 70.44%
class BrowserHistory:
    # O(1)
    def __init__(self, homepage: str):
        # Use two stacks to preserve back and forwards history.
        self.hist, self.f_hist = [homepage], []

    # O(1)
    def visit(self, url: str) -> None:
        # Push the url into the back stack and clear the forward stack.
        self.hist.append(url)
        if self.f_hist:
            self.f_hist = []

    # O(n) - Where n is the value of steps.
    def back(self, steps: int) -> str:
        while steps > 0 and len(self.hist) > 1:
            self.f_hist.append(self.hist.pop())
            steps -= 1
        return self.hist[-1]

    # O(n) - Where n is the value of steps.
    def forward(self, steps: int) -> str:
        while steps > 0 and self.f_hist:
            self.hist.append(self.f_hist.pop())
            steps -= 1
        return self.hist[-1]


# We can optimize the previous solution and make all operations run in
# O(1) time if we use only one stack and keep both ints, one to know
# the index of the element that we are at currently, the other to
# determine how many steps forward we can move at this time.
#
# Time complexity: O(1) - All operations are O(1).
# Space complexity: O(n) - Each call could result in one element added.
#
# Runtime 217 ms Beats 86.77%
# Memory 16.7 MB Beats 10.57%
class BrowserHistory2:
    def __init__(self, homepage: str):
        # Use a single stack and pointers.
        self.hist = [homepage]
        self.current_idx = 0
        self.can_move_forward = 0

    def visit(self, url: str) -> None:
        # Always move the current index and delete forward history.
        self.current_idx += 1
        self.can_move_forward = 0
        # If we are at the end of the history, append.
        if self.current_idx == len(self.hist):
            self.hist.append(url)
        else:
            self.hist[self.current_idx] = url

    def back(self, steps: int) -> str:
        # Compute the real number of steps we can take.
        real = min(steps, self.current_idx)
        self.current_idx -= real
        self.can_move_forward += real
        return self.hist[self.current_idx]

    def forward(self, steps: int) -> str:
        real = min(steps, self.can_move_forward)
        self.current_idx += real
        self.can_move_forward -= real
        return self.hist[self.current_idx]


def test():
    executors = [
        BrowserHistory,
        BrowserHistory2,
    ]
    tests = [
        [
            [
                "BrowserHistory",
                "visit",
                "visit",
                "visit",
                "back",
                "back",
                "forward",
                "visit",
                "forward",
                "back",
                "back",
            ],
            [
                ["leetcode.com"],
                ["google.com"],
                ["facebook.com"],
                ["youtube.com"],
                [1],
                [1],
                [1],
                ["linkedin.com"],
                [2],
                [2],
                [7],
            ],
            [
                None,
                None,
                None,
                None,
                "facebook.com",
                "google.com",
                "facebook.com",
                None,
                "linkedin.com",
                "google.com",
                "leetcode.com",
            ],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor(t[1][0][0])
                for i in range(1, len(t[0])):
                    call = t[0][i]
                    param = t[1][i][0]
                    result = getattr(sol, call)(t[1][i][0])
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
