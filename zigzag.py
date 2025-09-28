class Solution:
    def convert(self, s: str, numRows: int) -> str:
        temp_list: list[list[str]] = [[] for _ in range(numRows)]
        if numRows == 1:
            return s
        else:
            tracker: int = 0
            reverse: bool = False
            for char in s:
                if reverse is False and tracker < (numRows-1):
                    temp_list[tracker].append(char)
                    tracker += 1
                else:
                    reverse = True
                    if tracker > 0:
                        temp_list[tracker].append(char)
                        tracker -= 1
                    else:
                        temp_list[tracker].append(char)
                        tracker += 1
                        reverse = False
            result: list[str] = []
            for val in temp_list:
                result = result + val

            result = ''.join(result)
            return result

# The function convert takes a string s and an integer numRows as input and returns the string written in a zigzag pattern on a given number of rows.
# The algorithm uses a list of lists (temp_list) to store characters for each row.
# If numRows is 1, the function simply returns the original string since no zigzag pattern is needed.
# The algorithm iterates through each character in the string s, using a tracker to keep track of the current row and a reverse flag to determine the direction of movement (down or up).
# When moving down (reverse is False), characters are added to the current row, and the tracker is incremented until it reaches the last row.
# When moving up (reverse is True), characters are added to the current row, and the tracker is decremented until it reaches the first row.
# After processing all characters, the function concatenates the characters from each row in temp_list to form the final result string.
# Finally, the function returns the result string, which represents the zigzag pattern of the original string.
# Example: "PAYPALISHIRING", 3 -> "PAHNAPLSIIGYIR"
# Example: "PAYPALISHIRING", 4 -> "PINALSIGYAHRPI"
# Example: "A", 1 -> "A"