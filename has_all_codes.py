# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

from helpers import BColors


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        print(f'\n» Checking if {s} has all codes of size {k}')

        # possible_combinations = 2 ** k
        possible_combinations = 1 << k
        print(f'\n\tThere are {possible_combinations} possible combinations')

        # Inserting and finding characters in a set is O(1)
        found = set()
        for i in range(len(s) - k + 1):
            found.add(s[i:i+k])

        has_match = f'{BColors.ok_green}It is a match{BColors.end_dc}' if len(
            found) == possible_combinations else f'{BColors.fail}It is not a match{BColors.end_dc}'
        print(f'\tFound: {found}')
        print(
            f'\t{len(found)} out of {possible_combinations} combinations of size {k};\t {has_match}')

        return len(found) == possible_combinations

    def hasAllCodesBinary(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()

        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False


def test():
    print(
        f'\n{BColors.bold}{BColors.header}» ***** Testing hasAllCodes *****{BColors.end_dc}')
    sol = Solution()
    assert sol.hasAllCodes('00110110', 2) == True
    assert sol.hasAllCodes('00110', 2) == True
    assert sol.hasAllCodes('100', 2) == False
    assert sol.hasAllCodes('0110', 2) == False
    assert sol.hasAllCodes('0110', 1) == True
    assert sol.hasAllCodes('00110110', 1) == True
    assert sol.hasAllCodes('00110110', 4) == False
    print(f'\n{BColors.bold}{BColors.ok_green}» All tests passed!{BColors.end_dc}\n')


test()
