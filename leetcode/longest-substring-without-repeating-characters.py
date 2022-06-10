# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub, res = "", 0
        # Iterate over the characters in the string
        for ch in s:
            # If the current character is already in the substring
            if ch in sub:
                if len(sub) > res:
                    # Store the current substring length if it is the longest found
                    res = len(sub)
                # Split the string by the current character (match) and keep the leftmost part
                sub = sub.split(ch)[-1] + ch
            else:
                # If the current character is not already in the substring, add it
                sub += ch

        # Returning the maximum deals with the empty 's' case
        return max(res, len(sub))

    def lengthOfLongestSubstringPointer(self, s: str) -> int:
        seen = {}
        start = 0
        longest = 0
        for i, current in enumerate(s):
            if current in seen and start <= seen[current]:
                start = seen[current] + 1
            else:
                longest = max(longest, i - start + 1)
            seen[current] = i
        return longest

    def lengthOfLongestSubstringOn2(self, s: str) -> int:
        longest = 0
        if len(s) < 2:
            return len(s)
        for i in range(len(s)):
            if longest < len(s) - i:
                # Only keep going if we have more characters left than the longest match found
                found = set()
                for j in range(i, len(s)):
                    if s[j] not in found:
                        found.add(s[j])
                    else:
                        if len(found) > longest:
                            longest = len(found)
                        break

        return longest


def test():
    sol = Solution()
    tests = [
        # ['abcabcbb', 3],
        # ['bbbbb', 1],
        ['pwwkew', 3],
    ]
    for t in tests:
        assert sol.lengthOfLongestSubstring(
            t[0]) == t[1], f'{sol.lengthOfLongestSubstring(t[0])} != {t[1]}'


test()
