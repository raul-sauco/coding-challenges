# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


from collections import Counter
import timeit


# Runtime: 180 ms, faster than 72.96% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
# Memory Usage: 14.8 MB, less than 51.90 % of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
class NestedLoop:
    def minDeletions(self, s: str) -> int:
        c, d, r = Counter(s), 0, set()
        for f in c.values():
            while f > 0 and f in r:
                f -= 1
                d += 1
            r.add(f)
        return d


# Runtime: 389 ms, faster than 24.28% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
# Memory Usage: 15 MB, less than 7.85 % of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.


class HashMaps:
    def minDeletions(self, s: str) -> int:
        deletions, chars, fs = 0, {}, {}
        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        for f in chars:
            if chars[f] not in fs:
                fs[chars[f]] = 1
            else:
                fs[chars[f]] += 1
        for freq in range(max(chars.values()), 0, -1):
            if freq in fs and fs[freq] > 1:
                need_to_delete = fs[freq] - 1
                deletions += need_to_delete
                if freq - 1 in fs:
                    fs[freq-1] += need_to_delete
                else:
                    fs[freq-1] = need_to_delete
        return deletions


# Using Counter improves performance
class CounterAndLoops:
    def minDeletions(self, s: str) -> int:
        deletions, fs = 0, {}
        # chars = {k: s.count(k) for k in 'abcdefghijklmnopqrstuvwxyz'}
        chars = Counter(s)
        for f in chars:
            if chars[f] not in fs:
                fs[chars[f]] = 1
            else:
                fs[chars[f]] += 1
        for freq in range(max(chars.values()), 0, -1):
            if freq in fs and fs[freq] > 1:
                need_to_delete = fs[freq] - 1
                deletions += need_to_delete
                if freq - 1 in fs:
                    fs[freq-1] += need_to_delete
                else:
                    fs[freq-1] = need_to_delete
        return deletions


def test():
    executor = [
        {'executor': NestedLoop, 'title': 'NestedLoop', },
        {'executor': CounterAndLoops, 'title': 'CounterAndLoops', },
        {'executor': HashMaps, 'title': 'HashMaps', },
    ]
    tests = [
        ["abcdefghijklmnopqrstuvwxyz", 25],
        ["abbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjjkkkkkkkkkkkllllllllllllmmnnnoooopppppqqqqqqrrrrrrrsssssssstttttttttuuuuuuuuuuvvvvvvvvvvvwwwwwwwwwwwwwwxxxxxxxxxxxxxyyyyyyyyyyyyyz", 79],
        ["aab", 0],
        ["aaabbbcc", 2],
        ["ceabaacb", 2],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = int(sol.minDeletions(t[0]))
                expected = t[1]
                assert result == expected, f'{result} != {expected} for {t[0]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
