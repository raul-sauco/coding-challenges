# https://leetcode.com/problems/short-encoding-of-words/

import timeit
from typing import List

# Naive solution. Possible because len(words) < 2000
# Reverse the list of words O(n*log(n)) then iterate over them in O(n) and, if not covered by the
# last case add the current item + '#' positions to the result set.
#
# Runtime: 179 ms, faster than 79.54% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 14.4 MB, less than 100.00 % of Python3 online submissions for Short Encoding of Words.
#
# Locally this solution is more performant than SetSolution. With 1e6 runs of the current tests
# taking 1.32 seconds vs 1.96 for SetSolution. TrieSolution takes 2.42 seconds.


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # Sort the list from end to start in reverse order
        words.sort(key=lambda x: (x[::-1]), reverse=True)
        # Make sure the first word gets added to the result set
        last = ''
        result = 0
        for current in words:
            # If the current case is not covered by the last case, count it
            if not last.endswith(current):
                result += len(current)+1
                last = current
        return result


# Lee215's set solution here:
# https://leetcode.com/problems/short-encoding-of-words/discuss/125811/C%2B%2BJavaPython-Easy-Understood-Solution-with-Explanation
#
# Runtime: 135 ms, faster than 93.95% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 14.7 MB, less than 66.05 % of Python3 online submissions for Short Encoding of Words.


class SetSolution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)


# Lee215's Trie solution here:
# https://leetcode.com/problems/short-encoding-of-words/discuss/125784/Trie-Solution
#
# Runtime: 231 ms, faster than 65.58% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 16 MB, less than 59.53 % of Python3 online submissions for Short Encoding of Words.


class TrieSolution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = {}
        leaves = []
        for word in set(words):
            cur = root
            for i in word[::-1]:
                cur[i] = cur = cur.get(i, {})
            leaves.append((cur, len(word) + 1))
        return sum(depth for node, depth in leaves if len(node) == 0)


def test():
    executor = [
        {'executor': Solution, 'title': 'Naive Solution', },
        {'executor': SetSolution, 'title': 'Set Solution', },
        {'executor': TrieSolution, 'title': 'Trie Solution', },
    ]
    tests = [
        [["time", "me", "bell"], 10],   # "time#bell#"
        [["t"], 2],  # "t#"
        [[], 0],  # ""
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(1000000):
            for t in tests:
                sol = e['executor']()
                result = sol.minimumLengthEncoding(t[0])
                assert result == t[1], f'{result} != {t[1]}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
