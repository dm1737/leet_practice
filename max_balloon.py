from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        target = {'b','a','l','o','n'}
        for t in target:
            counts[t] = 0
        l = 0
        o = 0
        for c in text:
            if c in target:
                if c != 'l' and c != 'o':
                    counts[c] += 1
                else:
                    if c == 'l' and l == 0:
                        l += 1
                    elif c == 'l' and l > 0: 
                        counts[c] += 1
                        l -= 1
                    elif c == 'o' and o == 0:
                        o += 1
                    else:
                        counts[c] += 1
                        o -= 1
        return min(counts.values())
  