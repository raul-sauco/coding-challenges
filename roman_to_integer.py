class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store all Roman Symbols
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # Initialize the result
        num = 0
        # Iterate through the Roman string
        for i in range(len(s)):
            # If we are on the last symbol of the string
            if i == len(s) - 1:
                # Add the current symbol to the result
                num += roman_dict[s[i]]
            # If we are not on the last symbol of the string
            else:
                # If the current's symbol value is greater than the next's symbol value
                if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                    # Add the current symbol to the result
                    num += roman_dict[s[i]]
                # If the current symbol value is less than the next's symbol value
                else:
                    # Subtract the current symbol from the result
                    num -= roman_dict[s[i]]
        # Return the result
        return num

def test():
    sol =  Solution()
    assert sol.romanToInt("III") == 3
    assert sol.romanToInt("IV") == 4
    assert sol.romanToInt("IX") == 9
    assert sol.romanToInt("LVIII") == 58
    assert sol.romanToInt("MCMXCIV") == 1994

test()
