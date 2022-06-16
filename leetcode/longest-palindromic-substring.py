# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in [i, i+1]:
                # Reinitialize the indexes
                l = i
                r = j
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                current_longest = s[l+1:r]
                if len(current_longest) > len(longest):
                    longest = current_longest

        return longest

    def longestPalindromeDP(self, s: str) -> str:
        if not hasattr(self, 'dp'):
            self.dp = {}
        elif s in self.dp:
            return self.dp[s]
        if s == s[::-1]:
            return s
        left_trimmed = self.longestPalindrome(s[1:])
        right_trimmed = self.longestPalindrome(s[:-1])
        if len(left_trimmed) >= len(right_trimmed):
            self.dp[s] = left_trimmed
            return left_trimmed
        else:
            self.dp[s] = right_trimmed
            return right_trimmed


def test():
    tests = [
        ["babad", ["bab", "aba"]],
        ["cbbd", ["bb"]],
        ["abbcccbbbcaaccbababcbcabca", ["cbababc", "bbcccbb"]],
        ["iopsajhffgvrnyitusobwcxgwlwniqchfnssqttdrnqqcsrigjsxkzcmuoiyxzerakhmexuyeuhjfobrmkoqdljrlojjjysfdslyvckxhuleagmxnzvikfitmkfhevfesnwltekstsueefbrddxrmxokpaxsenwlgytdaexgfwtneurhxvjvpsliepgvspdchmhggybwupiqaqlhjjrildjuewkdxbcpsbjtsevkppvgilrlspejqvzpfeorjmrbdppovvpzxcytscycgwsbnmspihzldjdgilnrlmhaswqaqbecmaocesnpqaotamwofyyfsbmxidowusogmylhlhxftnrmhtnnljjhhcfvywsqimqxqobfsageysonuoagmmviozeouutsiecitrmkypwknorjjiaasxfhsftypspwhvqovmwkjuehujofiabznpipidhfxpoustquzyfurkcgmioxacleqdxgrxbldcuxzgbcazgfismcgmgtjuwchymkzoiqhzaqrtiykdkydgvuaqkllbsactntexcybbjaxlfhyvbxieelstduqzfkoceqzgncvexklahxjnvtyqcjtbfanzgpdmucjlqpiolklmjxnscjcyiybdkgitxnuvtmoypcdldrvalxcxalpwumfx", ["ykdky"]],
    ]
    sol = Solution()
    for t in tests:
        result = sol.longestPalindrome(t[0])
        assert result in t[1], f'{result} not in {t[1]}'


test()
