class Solution:
    def longest_palindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in a given string.
        Args:
            s (str): The input string to be evaluated.
        Returns:
            str: The longest palindromic substring found within the input string.
        """
        def expand_around_center(s: str, left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        n = len(s)
        if n == 0:
            return ""
        start, end = 0, 0
        for i in range(n):
            len1 = expand_around_center(s, i, i)
            len2 = expand_around_center(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]


# The function longestPalindrome takes a string s as input and returns the longest palindromic substring within s.
# The algorithm follows these steps:
# 1. Initialize variables to track the start and end indices of the longest palindrome found.
# 2. Iterate through each character in the string, treating each character (and the gap between characters) as potential centers for palindromes.
# 3. Expand around the center(s) to find the longest palindrome for each center.
# 4. Update the start and end indices if a longer palindrome is found.
# 5. Return the longest palindromic substring using the start and end indices.