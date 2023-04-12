# 71. Simplify Path
# 🟠 Medium
#
# https://leetcode.com/problems/simplify-path/
#
# Tags: String - Stack

import re
import timeit


# First merge contiguous directory separators into one, then split by
# directory separators. Iterate over the resulting directories or ".."
# elements, when we see "." we don't do anything, when we see a ".." we
# "travel" one directory up by popping the last element on the stack,
# anything else we consider a directory name and we push into the stack.
#
# Time complexity: O(n) - Cleaning and tokenizing the input needs to
# visit each character of the input path.
# Space complexity: O(n) - The stack can have as many characters as the
# input.
#
# Runtime 35 ms Beats 58.39%
# Memory 13.8 MB Beats 69.41%
class Solution:
    def simplifyPath(self, path: str) -> str:
        # Step 1 combine multiple '////' into '/'
        clean = re.sub(r"/+", "/", path)
        # Step 2 split into directory names.
        # https://stackoverflow.com/a/34844548/2557030
        tokens = [token for token in clean.split("/") if token]
        # Use a stack to store directory names
        stack = []
        for token in tokens:
            if token == ".":
                continue
            if token == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(token)
        return "/" + "/".join(stack)


def test():
    executors = [Solution]
    tests = [
        ["/../", "/"],
        ["/a/..", "/"],
        ["/a/../", "/"],
        ["/home/", "/home"],
        ["/abc/...", "/abc/..."],
        ["/a/./b/../../c/", "/c"],
        ["/a/../.././../../", "/"],
        ["/../../../../../a", "/a"],
        ["/home//foo/", "/home/foo"],
        ["/a//b//c//////d", "/a/b/c/d"],
        ["/a/./b/./c/./d/", "/a/b/c/d"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.simplifyPath(t[0])
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
