# 609. Find Duplicate File in System
# 🟠 Medium
#
# https://leetcode.com/problems/find-duplicate-file-in-system/
#
# Tags: Array - Hash Table - String

import timeit
from collections import defaultdict
from typing import List


# Use a dictionary to store file paths indexed by their content. Return
# the paths for any content found in more than one path.
#
# Time complexity: O(n) - We visit each path once.
# Space complexity: O(n) - The dictionary will grow to the size of the
# input.
#
# Runtime: 114 ms, faster than 79.66%
# Memory Usage: 24 MB, less than 54.58%
class HashTable:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # Use a default dictionary to store file paths indexed by their
        # content.
        d = defaultdict(list)
        # Iterate over the input paths processing their contents.
        for path in paths:
            # The first token contains the base path.
            base, *files = path.split()
            base += "/"
            for file in files:
                # Split the file name from its content.
                name, content = file.split("(")
                # We could, but don't need to, trim the last ")" from
                # the content: content = content[:-1]
                # Add this path to the dictionary.
                d[content].append(base + name)
        # Return any dictionary entries that have more than one path.
        return [d[k] for k in d if len(d[k]) > 1]


def test():
    executors = [HashTable]
    tests = [
        [
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
                "root 4.txt(efgh)",
            ],
            [
                ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
                ["root/a/1.txt", "root/c/3.txt"],
            ],
        ],
        [
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
            ],
            [
                ["root/a/2.txt", "root/c/d/4.txt"],
                ["root/a/1.txt", "root/c/3.txt"],
            ],
        ],
        [
            [
                "root/a 1.txt(abcd) 2.txt(fgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
            ],
            [["root/a/1.txt", "root/c/3.txt"]],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.findDuplicate(t[0])
                result.sort()
                exp = t[1]
                exp.sort()
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
