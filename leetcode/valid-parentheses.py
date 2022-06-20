# https://leetcode.com/problems/valid-parentheses/


from collections import deque
import timeit


# Using a stack
#
# Runtime: 37 ms, faster than 78.17% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14 MB, less than 23.82 % of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        closing = {')': "(", ']': "[", '}': "{"}
        for c in s:
            if c in closing:
                # Needs to match the last opening character
                if not st or closing[c] != st.pop():
                    return False
            else:
                st.append(c)
        return not st


# This solution runs slightly faster checking against a string and using only one dictionary,
# but the difference is negligible.
class FasterSolution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
        return stack == []


def test():
    sol = Solution()
    assert sol.isValid("()[]{}")
    assert sol.isValid("")
    assert sol.isValid("([{{{[()]}}}])[{{()}}]{[[(({{}}))]]}")
    assert not sol.isValid("(]")
    assert not sol.isValid("()[]{")
    assert not sol.isValid("(")
    assert not sol.isValid("]")


def test():
    executor = [
        {'executor': Solution, 'title': 'Solution', },
        {'executor': FasterSolution, 'title': 'Faster Solution', },
    ]
    tests = [
        ["()[]{}", True],
        ["", True],
        ["([{{{[()]}}}])[{{()}}]{[[(({{}}))]]}", True],
        ["(]", False],
        ["()[]{", False],
        ["()[]{", False],
        ["(", False],
        ["]", False],
    ]
    for e in executor:
        start = timeit.default_timer()
        for _ in range(100000):
            for t in tests:
                sol = e['executor']()
                result = sol.isValid(t[0])
                assert result == t[1], f'{result} != {t[1]}'
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        print("{0:20}{1:10}{2:10}".format(e['title'], used, "seconds"))


test()
