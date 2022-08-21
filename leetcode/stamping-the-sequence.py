# 936. Stamping The Sequence
# 🔴 Hard
#
# https://leetcode.com/problems/stamping-the-sequence/
#
# Tags: String - Stack - Greedy - Queue

import timeit
from collections import defaultdict
from typing import List

# TODO study this problem, I just imported the solutions from
# https://leetcode.com/problems/stamping-the-sequence/discuss/189254/Python-Greedy-and-DFS
# here to have a look and try to understand the process to come up with
# the greedy solution.

# Runtime: 177 ms, faster than 80.60%
# Memory Usage: 14 MB, less than 89.55%
class Greedy:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m, t, s, res = (
            len(target),
            len(stamp),
            list(target),
            list(stamp),
            [],
        )

        def check(i):
            changed = False
            for j in range(m):
                if t[i + j] == "?":
                    continue
                if t[i + j] != s[j]:
                    return False
                changed = True
            if changed:
                t[i : i + m] = ["?"] * m
                res.append(i)
            return changed

        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= check(i)
        return res[::-1] if t == ["?"] * n else []


# Runtime: 1031 ms, faster than 13.43%
# Memory Usage: 17.4 MB, less than 31.34%
class DFS:
    def movesToStamp(self, stamp: str, target: str):
        if stamp[0] != target[0] or stamp[-1] != target[-1]:
            return []
        n, m = len(stamp), len(target)
        path = [0] * m
        pos = defaultdict(set)
        for i, c in enumerate(stamp):
            pos[c].add(i)

        def dfs(i, index):
            path[i] = index
            if i == m - 1:
                return index == n - 1
            nxt_index = set()
            if index == n - 1:  # rule 2
                nxt_index |= pos[target[i + 1]]
            elif stamp[index + 1] == target[i + 1]:  # rule 0
                nxt_index.add(index + 1)
            if stamp[0] == target[i + 1]:  # rule 1
                nxt_index.add(0)
            return any(dfs(i + 1, j) for j in nxt_index)

        def path2res(path):
            down, up = [], []
            for i in range(len(path)):
                if path[i] == 0:
                    up.append(i)
                elif i and path[i] - 1 != path[i - 1]:
                    down.append(i - path[i])
            return down[::-1] + up

        if not dfs(0, 0):
            return []
        return path2res(path)


def test():
    executors = [
        Greedy,
        DFS,
    ]
    tests = [
        ["abc", "ababc", [[0, 2]]],
        ["abca", "aabcaca", [[3, 0, 1], [0, 3, 1]]],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.movesToStamp(t[0], t[1])
                exp = t[2]
                assert result in exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
