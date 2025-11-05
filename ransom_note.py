from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = defaultdict(int)
        mag = defaultdict(int)
        
        
        for c in ransomNote:
            ransom[c] += 1
            
        for c in magazine:
            mag[c] +=1
            
        for val in ransom:
            if ransom[val] > mag[val]:
                return False
        
        return True