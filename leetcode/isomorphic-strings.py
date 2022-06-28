# https://leetcode.com/problems/isomorphic-strings/


import timeit


# Neat idea using set and zip
# {('e', 'a'), ('g', 'd')}
#
#
# Runtime: 35 ms, faster than 98.43% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.2 MB, less than 44.28 % of Python3 online submissions for Isomorphic Strings.
class Zip:
    def isIsomorphic(self, s: str, t: str) -> bool:
        se = set(zip(s, t))
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


# Runtime: 73 ms, faster than 34.91% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.2 MB, less than 88.28 % of Python3 online submissions for Isomorphic Strings.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hs, ht = {}, {}
        l = len(s)
        if l != len(t):
            return False
        for i in range(l):
            if s[i] in hs or t[i] in ht:
                if s[i] not in hs or t[i] not in ht or hs[s[i]] != ht[t[i]]:
                    return False
            else:
                hs[s[i]], ht[t[i]] = i, i
        return True


def test():
    executor = [
        {'executor': Zip, 'title': 'Zip', },
        {'executor': Solution, 'title': 'Solution', },
    ]
    tests = [
        ["egg", "add", True],
        ["foo", "bar", False],
        ["paper", "title", True],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(int(float('1e4'))):
            for t in tests:
                sol = e['executor']()
                result = sol.isIsomorphic(t[0], t[1])
                expected = t[2]
                assert result == expected, f'{result} != {expected} for {t[0]}:{t[1]} using {e["title"]} solution'
        used = str(round(timeit.default_timer() - start, 5))
        result = "{0:20}{1:10}{2:10}".format(e['title'], used, "seconds")
        print(f"\033[92m» {result}\033[0m")


test()
