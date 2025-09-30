class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = abs(x)
            x = str(x)[::-1]
            x = int(x)
            x = x * -1
        else:
            x = str(x)[::-1]
            x = int(x)

        if x < -2**31 or x > 2**31 - 1:
            return 0
        else:
            return x

# The function reverse takes an integer x as input and returns the integer obtained by reversing its digits.
# If x is negative, the function first converts it to its absolute value, reverses the digits, and then re-applies the negative sign.
# The algorithm converts the integer to a string, reverses the string using slicing, and then converts it back to an integer.
# The function checks if the reversed integer is within the 32-bit signed integer range (-2^31 to 2^31 - 1). If it is out of this range, the function returns 0.
# Finally, the function returns the reversed integer if it is within the valid range.