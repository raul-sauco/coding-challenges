# 394. Decode String
# 🟠 Medium
#
# https://leetcode.com/problems/decode-string/
#
# Tags: String - Stack - Recursion

import timeit
from typing import List


# Iterate over the input string, when a digit is found, extract the substring that the digit encloses and recursively
# call decodeString().
#
# Time complexity: O(n) - We visit each element of the input once.
# Space complexity: O(n) - We use a list that will grow in length depending on the input size and the number of
# repeated sequences in the input.
#
# Runtime: 59 ms, faster than 16.18% of Python3 online submissions for Decode String.
# Memory Usage: 14.1 MB, less than 19.84% of Python3 online submissions for Decode String.
class Recursive:
    def decodeString(self, s: str) -> str:

        # Define a function that decodes sections of the input string.
        def decode(chars: List[str]) -> List[str]:
            result = []
            idx = 0

            # Iterate over the characters checking which type they belong to: letter, digit or "[", "]"
            while idx < len(chars):
                # Get the character at idx.

                c = chars[idx]

                # Handle nested encoded sequences of the form \d+\[.+\]
                if c.isdigit():
                    # Append the first digit of the digits sequence \d+
                    k = [c]
                    idx += 1
                    c = chars[idx]
                    # Check if there are more digits and append them
                    while c.isdigit():
                        k.append(c)
                        idx += 1
                        c = chars[idx]

                    # Convert k from a List of char to an int
                    k = int("".join(k))

                    # Skip the opening bracket "["
                    idx += 1

                    # Start recording the substring that we want to process recursively.
                    substr = []

                    # Record the fact that we have one bracket in the stack.
                    stack = 1

                    # While the stack is not empty.
                    # Equivalent to saying while we have not closed the outermost bracket.
                    while stack:
                        c = chars[idx]
                        # If we have more opening brackets, stack them and append them to the substring.
                        if c == "[":
                            stack += 1
                            substr.append(c)
                        # Pop one opening bracket from the stack, if we are not on the opening one, append it.
                        elif c == "]":
                            stack -= 1
                            if stack:
                                substr.append(c)
                            else:
                                # If we have the matching outer closing bracket, process the full subsequence and
                                # do not advance the index.
                                result += decode(substr) * k
                                break
                        else:
                            # Append digits and letters to the substring.
                            substr.append(c)
                        idx += 1

                else:
                    result.append(chars[idx])

                idx += 1
            return result

        return "".join(decode(list(s)))


# If we use a stack, the solution becomes easier to read because it becomes easier to match bracket pairs, fetch
# the preceding digit, convert it to int and use it to generate the substring. Then we can append that to the
# stack and keep going.
#
# Time complexity: O(n) - We visit each element a maximum of k times, adding it to the stack, popping it, then
# adding it again as the reconstructed sequence for each nested loop. Since we know that the number of nested
# loops is < n/4, because declaring a loop needs 3 extra characters, the complexity cannot grow to n^2.
# Space complexity: O(n*k) - The stack will grow to the size of the output string.
#
# Runtime: 60 ms, faster than 14.46% of Python3 online submissions for Decode String.
# Memory Usage: 13.9 MB, less than 71.03% of Python3 online submissions for Decode String.
class Stack:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            # Append anything that is not a closing bracket to the stack.
            if c != "]":
                stack.append(c)
            # When we find a closing bracket, we know we have completed a subsequence, decode it.
            else:
                substr = ""
                # Travel up the stack until we find the opening bracket, building the substring.
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                # Pop the opening bracket.
                stack.pop()
                # Reconstruct k
                k = ""

                # Make sure we have values left in the stack and that the one we are going to pop is a digit.
                while stack and stack[-1].isdigit():
                    # Prepend to k
                    k = stack.pop() + k

                # Once we have reconstructed the sequence and the factor k, decode and append to the stack.
                stack.append(int(k) * substr)

        # The problem asks for a string result.
        return "".join(stack)


def test():
    executors = [Recursive, Stack]
    tests = [
        ["", ""],
        ["a", "a"],
        ["aaabcbc", "aaabcbc"],
        ["3[a]2[bc]", "aaabcbc"],
        ["3[a2[c]]", "accaccacc"],
        ["2[abc]3[cd]ef", "abcabccdcdcdef"],
        ["10[leetcode]", "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.decodeString(t[0])
                exp = t[1]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
