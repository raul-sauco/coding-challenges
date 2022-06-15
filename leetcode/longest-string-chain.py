# https://leetcode.com/problems/longest-string-chain/


from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        self.longest = 0
        word_dict = defaultdict(list)
        for wrd in words:
            word_dict[len(wrd)].append(wrd)

        def processWord(w: str):
            if w in dp:
                return dp[w]
            max_chained = 1
            for i in range(len(w)):
                sliced = w[:i] + w[i + 1:]
                if sliced in word_dict[len(sliced)]:
                    max_chained = max(max_chained, processWord(sliced)+1)
            dp[w] = max_chained
            self.longest = max(max_chained, self.longest)
            return max_chained

        for l in range(max(word_dict), 0, -1):
            for word in word_dict[l]:
                processWord(word)

        return self.longest

    def longestStrChainSmallToBig(self, words: List[str]) -> int:
        d = {}
        longest = 1
        for word in sorted(words, key=len):
            d[word] = 1
            print('» ', word)
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]
                print(prev)
                if prev in d:
                    d[word] = max(d[word], d[prev] + 1)
            longest = max(longest, d[word])
        return longest


def test():
    sol = Solution()
    tests = [
        [["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5],
        [["a", "b", "ba", "bca", "bda", "bdca"], 4],
        [["xbc", "pcxbcf", "xb", "abcd", "cxbc", "pcxbc", "p"], 5],
        [["xbc", "pcxbcf", "xb", "abcd", "cxbc", "pcxbc", "b", "p"], 6],
        [["abcd", "dbqca"], 1],
        [["a"], 1],
    ]
    for t in tests:
        result = sol.longestStrChain(t[0])
        assert result == t[1], f'{result} != {t[1]}'
        result = sol.longestStrChainEasierToRead(t[0])
        assert result == t[1], f'{result} != {t[1]}'


test()


class BruteForceSolution:
    def longestStrChain(self, words: List[str]) -> int:
        self.longest = 0
        word_dict = defaultdict(list)
        for word in words:
            word_dict[len(word)].append(word)

        def processWord(word: str, index: int, matches=0):
            sliced = word[:index] + word[index +
                                         1:] if index < len(word)-1 else word[:-1]
            for smaller in word_dict[len(sliced)]:
                if sliced == smaller:
                    matched = matches + 1
                    self.longest = max(self.longest, matched)
                    processWord(sliced, 0, matched)
            if index+1 < len(word):
                processWord(word, index+1, matches)

        for l in range(max(word_dict), 0, -1):  # Length of longest words
            for w in word_dict[l]:
                processWord(w, 0, 0)

        return self.longest
