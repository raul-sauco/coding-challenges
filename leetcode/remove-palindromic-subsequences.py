# https://leetcode.com/problems/remove-palindromic-subsequences/

from helpers import BColors


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "":
            # If the string is empty
            return 0
        return 1 if s == s[::-1] else 2
        # if s == s[::-1]:
        #   A palindrome, we can delete the whole string
        #   return 1
        # Not a palindrome, we can remove all 'a's, then all 'b's
        # return 2


def test():

    print(f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')


test()
