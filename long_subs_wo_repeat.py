from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            if s[right] in dic:
                left = max(dic[s[right]], left)
            ans = max(ans, right - left + 1)
            dic[s[right]] = right + 1
            
        return ans
        