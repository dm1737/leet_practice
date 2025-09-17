from typing import Dict


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters in a given string.
        Args:
            s (str): The input string to be evaluated.
        Returns:
            int: The length of the longest substring without repeating characters.
        Example:
            >>> length_of_longest_substring("abcabcbb")
            3
            >>> length_of_longest_substring("bbbbb")
            1
            >>> length_of_longest_substring("pwwkew")
            3
        """
        char_index_map: Dict[str, int] = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            current_char = s[right]

            if current_char in char_index_map and char_index_map[current_char] >= left:
                left = char_index_map[current_char] + 1

            char_index_map[current_char] = right
            current_length = right - left + 1
            max_length = max(max_length, current_length)

        return max_length

# The function length_of_longest_substring takes a string s as input and returns the length of the longest substring without repeating characters.
# The algorithm uses a sliding window approach with two pointers (left and right) to keep track of the current substring.
# A dictionary (char_index_map) is used to store the most recent index of each character in the string.
# The algorithm iterates through the string using the right pointer, and for each character:
#     If the character has been seen before and its index is within the current window (i.e., its index is greater than or equal to left), move the left pointer to one position after the last occurrence of that character.
#     Update the character's index in the dictionary to the current position (right).
#     Calculate the current length of the substring (right - left + 1) and update max_length if the current length is greater than max_length.
# Finally, the function returns max_length, which represents the length of the longest substring without repeating characters.