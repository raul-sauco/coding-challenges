# https://leetcode.com/problems/valid-anagram/

from collections import defaultdict


# Solution using string.count has a theoretical worst-case-scenario complexity of On^2 but it
# actually performs better on the LeetCode tests. I am not sure if this is due to the C
# implementation or the values that are being used on the tests, for example, if we fail with 'a'
# this test would run really fast
#
# Runtime: 48 ms, faster than 91.87% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4 MB, less than 96.95 % of Python3 online submissions for Valid Anagram.
#
#         for c in 'abcdefghijklmnopqrstuvwxyz':
#            if s.count(c) != t.count(c): return False
#         return True


# Solution using defaultdict(int) and chars[0] += 1
# Runtime: 62 ms, faster than 68.39% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.3 MB, less than 96.95 % of Python3 online submissions for Valid Anagram.

# Solution using return Counter(s) == Counter(t)
# Runtime: 70 ms, faster than 54.35% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.5 MB, less than 34.56 % of Python3 online submissions for Valid Anagram.

# Solution using chars.get(c, 0) + 1
# Runtime: 78 ms, faster than 41.83% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.6 MB, less than 34.56 % of Python3 online submissions for Valid Anagram.

# Solution using sorted(s) == sorted(t)
# Runtime: 83 ms, faster than 34.87% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.1 MB, less than 11.43 % of Python3 online submissions for Valid Anagram.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return sorted(s) == sorted(t)

        # return Counter(s) == Counter(t)

        # for c in 'abcdefghijklmnopqrstuvwxyz':
        #     if s.count(c) != t.count(c):
        #         return False
        # return True

        if len(s) != len(t):
            return False
        chars = defaultdict(int)
        # chars = {}
        for c in s:
            chars[c] += 1
            # chars[c] = chars.get(c, 0) +1
        for w in t:
            if w not in chars:
                return False
            chars[w] -= 1
            if chars[w] == 0:
                del chars[w]
        return True


def test():
    sol = Solution()
    assert sol.isAnagram(s="anagram", t="nagaram") == True
    assert sol.isAnagram(s="rat", t="car") == False
    assert sol.isAnagram(s="aacc", t="cacc") == False


test()
