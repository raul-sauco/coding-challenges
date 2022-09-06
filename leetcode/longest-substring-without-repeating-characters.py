# 3. Longest Substring Without Repeating Characters
# 🟠 Medium
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Tags: Hash Table - String - Sliding Window


import timeit


# We can reduce time complexity using a hash map that stores the indices
# keyed by the character. We iterate over the input checking if we have
# seen the same character before, instead of keeping the longest
# sequence seen as a substring, we only keep a reference to the current
# longest sequence start index. If we see a character that we have
# already seen, meaning that it is in the currently longest sequence, we
# update our sequence by moving the start index to the position right
# after the index of the leftmost duplicate character. We check the
# length of the current sequence using the start and current character
# indices.
#
# Time complexity: O(n) - We iterate over the input and, for each
# character, do O(1) work.
# Space complexity: O(n) - The dictionary can grow to the size of the
# input.
#
# Runtime: 59 ms, faster than 96.52%
# Memory Usage: 14 MB, less than 93.13%
class HashMapAndPointer:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Store characters that we have seen as dictionary keys, and the
        # index where we saw them as the value.
        seen = {}
        # Keep a pointer to the start index of the longest sequence seen.
        start = 0
        # Keep the length of the longest sequence seen.
        longest = 0
        # Iterate over the input string.
        for i, current in enumerate(s):
            # If we have seen the current character and it is still part
            # of the sequence that we are considering. If the index of
            # the previous occurrence is to the left of the sequence
            # that we are considering, we do not need to do anything.
            if current in seen and start <= seen[current]:
                # Trim the current string moving the start to the
                # right of the previous occurrence of this character.
                start = seen[current] + 1
            # We can use the current character in the sequence add it.
            else:
                longest = max(longest, i - start + 1)
            # In both cases, update the last seen index of this character.
            seen[current] = i
        # Return the longest sequence length seen.
        return longest

        # Shorter version without comments.
        # seen, start, longest = {}, 0, 0
        # for i in range(len(s)):
        #     c = s[i]
        #     if c in seen and start <= seen[c]:
        #         start = seen[c] + 1
        #     else:
        #         longest = max(longest, i - start + 1)
        #     seen[c] = i
        # return longest


# Store the maximum substring seen in a separate substring, for each
# character, check if it is in the substring, if found, trim the left
# section up to the other occurrence of the character and keep the
# right section adding the new occurrence. Return the max length seen.
#
# Time complexity: O(n^2) - We visit each character and, for each, can
# check if it is a duplicate in the substring that we are building, this
# can mean a nested O(n) cost.
# Space complexity: O(n) - The substring can grow to the same size as
# the input.
#
# Runtime: 86 ms, faster than 72.66%
# Memory Usage: 14.1 MB, less than 13.89%
class NestedLoops:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize an empty string and the max length seen.
        sub, res = "", 0
        # Iterate over the characters in the string. O(n)
        for ch in s:
            # If the current character is already in the substring. O(n)
            if ch in sub:
                if len(sub) > res:
                    # Store the current substring length if it is the
                    # longest found.
                    res = len(sub)
                # Split the string by the current character (match) and
                # keep the rightmost part, then add the current char.
                sub = sub.split(ch)[-1] + ch
            else:
                # If the current character is not already in the
                # substring, add it.
                sub += ch

        # Returning the maximum deals with the empty 's' case
        return max(res, len(sub))


# Other naive solution iterates over the characters using nested loops,
# the inner loop adds characters to a set until it finds a duplicate
# character, then exists.
#
# Time complexity: O(n^2)
# Space complexity: O(n)
#
# Runtime: 597 ms, faster than 14.89%
# Memory Usage: 14 MB, less than 49.64%
class Naive:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base case.
        if len(s) < 2:
            return len(s)
        # Store the max sequence length seen.
        longest = 0
        # Iterate over the input O(n)
        for i in range(len(s)):
            # Only keep going if we have more characters left than the
            # longest match found.
            if longest < len(s) - i:
                # Initialize a set.
                found = set()
                # Iterate over the input starting at the current
                # character, nested O(n)
                for j in range(i, len(s)):
                    # If we have not seen this character in the inner loop.
                    if s[j] not in found:
                        found.add(s[j])
                        longest = max(longest, len(found))
                    # If we have seen this character, compare the length
                    # of the current sequence with the best and exit.
                    else:
                        break
        # Return the max length seen.
        return longest


def test():
    executors = [
        HashMapAndPointer,
        NestedLoops,
        Naive,
    ]
    tests = [
        ["au", 2],
        ["abcabcbb", 3],
        ["bbbbb", 1],
        ["babbcbb", 2],
        ["pwwkew", 3],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(10000):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.lengthOfLongestSubstring(t[0])
                exp = t[1]
                assert result == exp, (
                    f"\033[93m» {result} <> {exp}\033[91m for"
                    + f" test {col} using \033[1m{executor.__name__}"
                )
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        cols = "{0:20}{1:10}{2:10}"
        res = cols.format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
