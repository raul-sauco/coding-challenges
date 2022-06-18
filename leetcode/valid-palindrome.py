# https://leetcode.com/problems/valid-palindrome/

# import re

# Solution using string.join and two pointers with a while loop
#
# Runtime: 43 ms, faster than 95.95% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.7 MB, less than 43.02 % of Python3 online submissions for Valid Palindrome.
#
#       l = "".join(filter(str.isalnum, s)).lower()
#       i = 0
#       j = len(l) - 1
#       while i < j:
#           if(l[i] != l[j]):
#               return False
#           j -= 1
#           i += 1
#       return True
#


# Solution using string.join and two pointers with a for/range
#
# Runtime: 47 ms, faster than 91.78% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.7 MB, less than 43.02 % of Python3 online submissions for Valid Palindrome.
#
#       l = "".join(filter(str.isalnum, s)).lower()
#       j = len(l) - 1
#       for i in range(len(l) // 2):
#            if(l[i] != l[j]):
#                return False
#            j -= 1
#        return True


# Solution using string.join and reversing the string
#
# Runtime: 47 ms, faster than 91.78% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.8 MB, less than 36.86 % of Python3 online submissions for Valid Palindrome.
#
#       l = "".join(filter(str.isalnum, s)).lower()
#       return l == l[::-1]
#


# Solution using compiled regex and reversing the string
#
# Runtime: 60 ms, faster than 68.44% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.3 MB, less than 23.03 % of Python3 online submissions for Valid Palindrome.
#
#       l = re.compile('[\W_]+').sub('', s).lower()
#       return l == l[::-1]
#


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = "".join(filter(str.isalnum, s)).lower()
        i = 0
        j = len(l) - 1
        while i < j:
            if(l[i] != l[j]):
                return False
            j -= 1
            i += 1
        return True


def test():
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama")
    assert not sol.isPalindrome("race a car")
    assert sol.isPalindrome(" ")
    assert not sol.isPalindrome("0P")


test()
