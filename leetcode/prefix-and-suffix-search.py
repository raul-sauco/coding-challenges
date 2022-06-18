# https://leetcode.com/problems/prefix-and-suffix-search/

from typing import List

# Runtime: 1297 ms, faster than 80.12% of Python3 online submissions for Prefix and Suffix Search.
# Memory Usage: 58.1 MB, less than 40.67 % of Python3 online submissions for Prefix and Suffix Search.


class WordFilter:

    def __init__(self, words: List[str]):
        self.root = {}
        for weight, w in enumerate(words):
            for i in range(len(w), -1, -1):
                t = w[i:] + "#" + w
                self.insert(t, weight)

    def insert(self, word: str, weight: int) -> None:
        current = self.root
        for w in word:
            if w not in current:
                current[w] = {}
            current = current[w]
            # Overwrite lesser weights in case of a collision
            current['.'] = weight

    def f(self, prefix: str, suffix: str) -> int:
        term = suffix + '#' + prefix
        current = self.root
        for w in term:
            if w not in current:
                return -1
            current = current[w]

        return current['.']

        # Your WordFilter object will be instantiated and called as such:
        # obj = WordFilter(words)
        # param_1 = obj.f(prefix,suffix)


def test():
    wf = WordFilter(["test", "apple"])
    assert wf.f('tes', 'st') == 0
    result = wf.f('a', 'e')
    assert result == 1, f'Apple is in position 1 not {result}'


test()
