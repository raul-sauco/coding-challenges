# 5. Longest Palindromic Substring
# 🟠 Medium
#
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Tags: String - Dynamic Programming


import timeit


# We can start looking for a solution by checking if the original string is a palindrome, if it isn't, do
# a recursive call with both the left-trimmed version and the right-trimmed version. This is a brute-force
# solution in which we are checking all possible substrings of the input string.
#
# Time complexity: O(n^3)
# Space complexity: O(1)
#
# This solution will fail with Time Limit Exceeded.
class BruteForce:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        # For each possible start and end index combination.
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i : j + 1]
                # Check if the string is a palindrome.
                if substr == substr[::-1] and len(substr) > len(longest):
                    # If the string is a palindrome, check if it is longer than the longest found so far.
                    longest = substr

        # Return any of the longest palindromes found in the string.
        return longest


# Improve on the previous solution storing substrings that we have already checked.
#
# Time complexity: O(n^2) - We still iterate over all possible substrings but only check if they are palindromes
# one time. This brings the complexity down.
# Space complexity: O(n^2) - The dictionary will contain all possible substrings in the input string.
class Memoized:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        memo = {}

        # For each possible start and end index combination.
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i : j + 1]
                if not substr in memo:
                    # We only need to memoize the fact that we checked the string.
                    memo[substr] = True
                    # Check if the string is a palindrome.
                    if substr == substr[::-1] and len(substr) > len(longest):
                        # If the string is a palindrome, check if it is longer than the longest found so far.
                        longest = substr

        # Return any of the longest palindromes found in the string.
        return longest


# We use the fact that palindromes are simetrical around their center, iterate over single characters, and pairs of
# characters, in s, and try to build palindromes expanding out from them. When we build the longest palindrome we
# can from each start position, we check it against the longest we have seen so far.
#
# Time complexity: O(n^2) - We are expanding each palindrome around its center O(n) 2* each position in the string 2n.
# Space complexity: O(1) - We are using a constant amount of extra memory, pointers to right and left index.
#
# Runtime: 1385 ms, faster than 59.78% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14 MB, less than 29.50% of Python3 online submissions for Longest Palindromic Substring.
class ExpandAroundCenter:
    def longestPalindrome(self, s: str) -> str:
        # We are guaranteed to have 1 character and so, at least, 1 palindrome.
        # Store indexes instead of the string.
        indexes = (0, 1)
        # Store also the current max_length to avoid doing the substraction r - l each time.
        max_length = 1

        # Iterate over every character in the string.
        for i in range(len(s)):
            # Try to build a palindrome starting at this character and the pair formed by this character and the next.
            for j in [i, i + 1]:
                # Reinitialize the indexes in each iteration.
                l, r = i, j
                # While we are within the boundaries of the string and the characters we just added match.
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                # The longest palindrome we could build is (l+1, r-1)
                l += 1
                # r -= 1 Making the index point to the next character after the palindrome makes slicing easier.
                current_length = r - l
                if current_length > max_length:
                    max_length = current_length
                    indexes = (l, r)

        return s[indexes[0] : indexes[1]]


# We can improve the solution even further and achieve linear running time using Manacher's Algorithm.
#
# https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
#
# Time complexity: O(n) - We visit each element in the string once.
# Space complexity: O(n) - The memory use will grow linearly with the size of the input.
#
# Runtime: 248 ms, faster than 95.66% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.1 MB, less than 29.50% of Python3 online submissions for Longest Palindromic Substring.
class Manacher:
    def longestPalindrome(self, s: str) -> str:
        # Insert an extra character between each character in s.
        ss = "." + ".".join(s) + "."
        # Keep track of the longest palindrome we can build around each position of ss.
        # len(ss) == len(palindrome_radii) == 2 * len(s) + 1
        palindrome_radii = [0] * len(ss)

        center = radius = 0

        # Iterate over the characters in s.
        while center < len(ss):

            # At the start of the loop, radius is already set to a lower-bound for the longest radius.
            # In the first iteration, radius is 0, but it can be higher.

            # Determine the longest palindrome starting at center-radius and going to center+radius.
            while (
                center - (radius + 1) >= 0
                and center + (radius + 1) < len(ss)
                and ss[center - (radius + 1)] == ss[center + (radius + 1)]
            ):
                radius += 1

            # Save the radius of the longest palindrome in the array.
            palindrome_radii[center] = radius

            # Below, center is incremented.
            # If any precomputed values can be reused, they are.
            # Also, radius may be set to a value greater than 0.

            old_center = center
            old_radius = radius
            center += 1
            # Radius' default value will be 0, if we reach the end of the following loop.
            radius = 0
            while center <= old_center + old_radius:
                # Because center lies inside the old palindrome and every character inside a palindrome has a
                # "mirrored" character reflected across its center, we can use the data that was precomputed for
                # the Center's mirrored point.
                mirrored_center = old_center - (center - old_center)
                max_mirrored_radius = old_center + old_radius - center
                if palindrome_radii[mirrored_center] < max_mirrored_radius:
                    palindrome_radii[center] = palindrome_radii[mirrored_center]
                    center += 1

                elif palindrome_radii[mirrored_center] > max_mirrored_radius:
                    palindrome_radii[center] = max_mirrored_radius
                    center += 1

                # palindrome_radii[mirrored_center] = max_mirrored_radius
                else:
                    radius = max_mirrored_radius
                    break  # exit while loop early

        # The original algorithm returns the length of the longest palindrome.
        # longest_palindrome_in_ss = max(palindrome_radii)
        # longest_palindrome_in_s = (longest_palindrome_in_ss - 1) / 2

        # Modify it to return the longest palindrome itself.
        max_length = max(palindrome_radii)
        start = (palindrome_radii.index(max_length) - max_length) // 2
        end = start + max_length
        return s[start:end]


def test():
    executors = [
        # ExpandAroundCenter,
        # BruteForce,
        # Memoized,
        Manacher,
    ]
    tests = [
        ["babad", ["bab", "aba"]],
        ["cbbd", ["bb"]],
        ["abbcccbbbcaaccbababcbcabca", ["cbababc", "bbcccbb"]],
        [
            "iopsajhffgvrnyitusobwcxgwlwniqchfnssqttdrnqqcsrigjsxkzcmuoiyxzerakhmexuyeuhjfobr"
            + "mkoqdljrlojjjysfdslyvckxhuleagmxnzvikfitmkfhevfesnwltekstsueefbrddxrmxokpaxsenwl"
            + "gytdaexgfwtneurhxvjvpsliepgvspdchmhggybwupiqaqlhjjrildjuewkdxbcpsbjtsevkppvgilrl"
            + "spejqvzpfeorjmrbdppovvpzxcytscycgwsbnmspihzldjdgilnrlmhaswqaqbecmaocesnpqaotamwo"
            + "fyyfsbmxidowusogmylhlhxftnrmhtnnljjhhcfvywsqimqxqobfsageysonuoagmmviozeouutsieci"
            + "trmkypwknorjjiaasxfhsftypspwhvqovmwkjuehujofiabznpipidhfxpoustquzyfurkcgmioxacle"
            + "qdxgrxbldcuxzgbcazgfismcgmgtjuwchymkzoiqhzaqrtiykdkydgvuaqkllbsactntexcybbjaxlfh"
            + "yvbxieelstduqzfkoceqzgncvexklahxjnvtyqcjtbfanzgpdmucjlqpiolklmjxnscjcyiybdkgitxn"
            + "uvtmoypcdldrvalxcxalpwumfxmhtnnljjhhcfvywsqimqxqobfsageysonmhtnnljjhhcfvywsqimqx",
            ["ykdky"],
        ],
    ]
    for executor in executors:
        start = timeit.default_timer()
        for _ in range(int(float("1"))):
            for col, t in enumerate(tests):
                sol = executor()
                result = sol.longestPalindrome(t[0])
                exp = t[1]
                assert (
                    result in exp
                ), f"\033[93m» {result} not in {exp}\033[91m for test {col} using \033[1m{executor.__name__}"
        stop = timeit.default_timer()
        used = str(round(stop - start, 5))
        res = "{0:20}{1:10}{2:10}".format(executor.__name__, used, "seconds")
        print(f"\033[92m» {res}\033[0m")


test()
