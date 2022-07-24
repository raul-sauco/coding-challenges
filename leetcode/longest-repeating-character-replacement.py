# 424. Longest Repeating Character Replacement
# 🟠 Medium
#
# https://leetcode.com/problems/longest-repeating-character-replacement/
#
# Tags: Hash Table - String - Sliding Window

import timeit
from collections import Counter, defaultdict


# Use two pointers. For each window, check if we can make all characters in the current window the same using
# the replacements allowed by k. If we can, check if we need to update the best result and move the right
# pointer, if we cannot, shrink the window by moving the left pointer.
# To check if we can make all characters in the current sliding window the same, we can use a Counter, if
# the sum of the most common character in the counter + k is equal or greater than the length of the current
# window, we can make all characters the same, if is lesser, we cannot.
#
# Time complexity: O(n) - We visit each character once.
# Space complexity: O(1) - The Counter is indexed by character, it has a max size of 26.
#
# Runtime: 305 ms, faster than 21.80% of Python3 online submissions for Longest Repeating Character Replacement.
# Memory Usage: 14 MB, less than 57.73% of Python3 online submissions for Longest Repeating Character Replacement.
class SlidingWindow:
    def characterReplacement(self, s: str, k: int) -> int:
        # We will always have a minimum of 1 character in s.
        result = k + 1
        # If the length of s is less than what we have already, return.
        if len(s) < result:
            return len(s)

        # Otherwise initialize two pointers and start visiting a window of size > result
        left, right = 0, 0
        # Use a counter to access the highest value easily.
        counter = Counter([s[0]])
        while right < len(s):
            # Check if it is possible to make all characters in this window the same.
            window_size = right + 1 - left
            if max(counter.values()) + k >= window_size:
                # If the count of the most frequent character in the counter + k is equal or bigger than the current window, we can
                # make all the characters in the current window the same.
                result = max(result, window_size)

                # Advance the right pointer.
                right += 1
                if right < len(s):
                    # Check if we have gone over the right boundary, an add the character at the right pointer.
                    counter[s[right]] += 1
            else:
                # We cannot make all characters in this sequence equal, it won't be possible either expanding to the right.
                # We shrink the window from the left. Remove the character at left from the counter and update the pointer.
                counter[s[left]] -= 1
                left += 1

        return result


def test():
    executors = [SlidingWindow]
    tests = [
        ["ABAB", 2, 4],
        ["AABABBA", 1, 4],
        ["AABABBA", 0, 2],
        ["AABBBBA", 0, 4],
        ["ABACBADEF", 0, 1],
        ["A", 10, 1],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.characterReplacement(t[0], t[1])
                exp = t[2]
                assert (
                    result == exp
                ), f"\033[93m» {result} <> {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
