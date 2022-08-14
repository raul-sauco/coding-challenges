# 76. Minimum Window Substring
# 🔴 Hard
#
# https://leetcode.com/problems/minimum-window-substring/
#
# Tags: Hash Table - String - Sliding Window

import timeit
from collections import Counter


# Use a counter to get the count of the characters in t, then use a
# sliding window to start checking characters in s, we increase the
# window on the right checking the characters that we find until we
# run out of characters or find all the ones that we need. If we find
# all characters in t, we check if the current window is the smallest
# that we have seen so far and save its length, then start shrinking the
# window from the left until it no longer satisfies the condition, then
# start increasing from the right again.
#
# Time complexity: O(n) - We only visit each element once to add it to
# the count of elements seen and once to remove it. For each element,
# we check if we have a full match in O(1)
# Space complexity: O(n) - The dictionary can grow to the size of the
# input.
#
# Runtime: 521 ms, faster than 14.04%
# Memory Usage: 14.8 MB, less than 10.72%
class Count:
    def minWindow(self, s: str, t: str) -> str:
        # If t is longer than s, there is no solution.
        if len(t) > len(s):
            return ""
        # Store the index and the length of the shortest substring found
        # so far in s that contains all the characters in t.
        min_window = (-1, float("inf"))
        # Add all the character frequencies in t to a dictionary of
        # characters that we are missing.
        freq = Counter(t)
        # Initialize our two pointers at the leftmost index.
        left = right = 0
        # Since t has a min length of 1, we will be missing some
        # character at the start of the iterations.
        m = True
        # Keep iterating as long as we either have more characters to
        # explore moving the right pointer or can shrink the window
        # moving the left pointer.
        while right < len(s) or not m:
            if m:
                # Check the character under the right pointer.
                # Take care of the edge case when we have gone past the
                # end of the array and just want to allow the left
                # pointer to catch up.
                if s[right] in freq:
                    freq[s[right]] -= 1
                right += 1
            else:
                # The current window contains all characters in t
                # save its length and index and move the left pointer.
                current_window_length = right - left
                if current_window_length < min_window[1]:
                    min_window = (left, current_window_length)
                # Move the left pointer.
                if s[left] in freq:
                    freq[s[left]] += 1
                left += 1
            # Check if we are missing any characters. Since the
            # dictionary has a max size of 52, this is O(1).
            m = False
            for c in freq:
                if freq[c] > 0:
                    m = True
                    break

        # Return the minimum substring or ""
        if min_window[1] == float("inf"):
            return ""
        return s[min_window[0] : min_window[0] + min_window[1]]


# Small optimization to the previous solution where we store the number
# of characters that we are missing to have a full match. Instead of
# iterating over the whole dictionary each time, we just need to check
# one value.
#
# Time complexity: O(n)
# Space complexity: O(1)
#
# Runtime: 136 ms, faster than 71.76%
# Memory Usage: 14.8 MB, less than 36.34%
class CounterAndMatched:
    def minWindow(self, s: str, t: str) -> str:
        # If t is longer than s, there is no solution.
        if len(t) > len(s):
            return ""
        # Store the index and the length of the shortest substring found
        # so far in s that contains all the characters in t.
        min_window = (-1, float("inf"))
        # Add all the character frequencies in t to a dictionary of
        # characters that we are missing.
        freq = Counter(t)
        # Initialize our two pointers at the leftmost index.
        left = right = 0
        # Count the number of unique characters that we need to find.
        m = len(freq)
        # Keep iterating as long as we either have more characters to
        # explore moving the right pointer or can shrink the window
        # moving the left pointer.
        while right < len(s) or m == 0:
            # If we still need to find some characters. m > 0
            if m:
                # Check the character under the right pointer.
                # Take care of the edge case when we have gone past the
                # end of the array and just want to allow the left
                # pointer to catch up.
                if s[right] in freq:
                    freq[s[right]] -= 1
                    # If the number of this character that we still need
                    # has become 0, we don't need to find it any longer.
                    if freq[s[right]] == 0:
                        m -= 1
                right += 1
            else:
                # The current window contains all characters in t
                # save its length and index and move the left pointer.
                current_window_length = right - left
                if current_window_length < min_window[1]:
                    min_window = (left, current_window_length)
                # Move the left pointer.
                if s[left] in freq:
                    freq[s[left]] += 1
                    # If the number of this character that we still need
                    # has become 1, we need to find one.
                    if freq[s[left]] == 1:
                        m += 1
                left += 1

        # Return the minimum substring or ""
        if min_window[1] == float("inf"):
            return ""
        return s[min_window[0] : min_window[0] + min_window[1]]


def test():
    executors = [
        Count,
        CounterAndMatched,
    ]
    tests = [
        ["ADOBECODEBANC", "ABC", "BANC"],
        ["aADOBECODEBANC", "ABCa", "aADOBEC"],
        ["a", "a", "a"],
        ["a", "b", ""],
        ["a", "aa", ""],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(1):
            for n, t in enumerate(tests):
                sol = executor()
                result = sol.minWindow(t[0], t[1])
                exp = t[2]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for "
                    + f"test {n} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
