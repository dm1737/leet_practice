class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == '' or s == "" or s == '-' or s == "-" or s == '+':
            return 0
        sign = 0
        result = ''
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        else:
            sign = 0
        for char in s:
            try: 
                test = int(char)
                result += char
            except:
                if result == '':
                    return 0
                if sign == -1: 
                    result = int(result) * sign
                result = int(result)
                if result < -(2**31): 
                    return -(2**31)
                elif result > 2**31 - 1:
                    return  (2**31) -1
                else: 
                    return result
        result = int(result)
        if sign == -1:
            result = result * sign
        if result < -(2**31): 
            return -(2**31)
        elif result > 2**31 - 1:
            return  (2**31) -1
        else: 
            return result
# The function myAtoi converts a string s to a 32-bit signed integer (similar to C/C++'s atoi function).
# It first trims any leading or trailing whitespace from the string. If the string is empty or contains only a sign without digits, it returns 0.
# The function checks for an optional sign ('-' or '+') at the beginning of the string and sets the sign accordingly.
# It then iterates through the characters of the string, attempting to convert each character to an integer. If a character is not a digit, the function stops processing further characters.
# If no digits were found before encountering a non-digit character, the function returns 0. If digits were found, it converts the accumulated string of digits to an integer and applies the sign if necessary.
# The function checks if the resulting integer is within the 32-bit signed integer range (-2^31 to 2^31 - 1). If it is out of this range, it returns the appropriate boundary value. 
# Finally, the function returns the converted integer if it is within the valid range. 
# The function uses try-except blocks to handle non-digit characters and ensure robust conversion.