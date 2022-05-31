# https://leetcode.com/problems/divide-two-integers/

min_allowed = -2147483648
max_allowed = 2147483647

def to_binary_list(int_base_10):
    #convert an int base 10 to a list of 0's and 1's
    return [int(x) for x in bin(int_base_10)[2:]]

class Solution:
    # This solution is based on the fact that the quotient of a division is equal to the number
    # of times the divisor goes into the dividend. 
    # We can use bitwise operations to get the quotient.
    def divide(self, dividend: int, divisor: int) -> int:
        param_dividend = dividend
        param_divisor = divisor

        # Determine if the result will be negative
        negative = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        
        # The problem has a constraint of -2147483648 to 2147483647
        upper_bound = 1 << 31 if negative else (1 << 31) -1
        
        # Equivalent to using abs()
        dividend = 0 - dividend if dividend < 0 else dividend
        divisor = 0 - divisor if divisor < 0 else divisor
        
        # Convert the dividend to a binary list
        dividend = [int(x) for x in bin(dividend)[2:]]
        
        current_dividend = 0
        result = 0

        print(f'\n» Dividing {param_dividend} by {param_divisor}\n')
        for next_digit in dividend:
            current_dividend = (current_dividend << 1) + next_digit

            if(divisor <= current_dividend):
                current_dividend -= divisor
                new_digit = 1
            else:
                new_digit = 0
            
            result = (result << 1) + new_digit
            print(f'current dividend: {current_dividend}; result: {result}; new digit: {new_digit}')
        
        result = min(result, upper_bound)
        if(negative):
            result = 0 - result

        print(f'\n» The result of {param_dividend} / {param_divisor} is {result}\n')
        
        return result

        
    def divide_slow(self, dividend: int, divisor: int) -> int:
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        return quotient * sign

def test(): 
    sol = Solution()
    assert sol.divide(10, 3) == 3
    assert sol.divide(7, -3) == -2
    assert sol.divide(1, 1) == 1
    assert sol.divide(0, 1) == 0
    assert sol.divide(min_allowed, -1) == max_allowed
    assert sol.divide(1 << 31, 1) == max_allowed
    assert sol.divide(1 << 31, -17) == -126322567
    print('All tests passed!')

test()

# Uncomment the following lines to see print statements
# sol=Solution()
# sol.divide(1 << 31, 17)