class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_test = set()
        for c in jewels:
            j_test.add(c)
            
        j_count = 0
        for s in stones:
            if s in j_test:
                j_count += 1
                
        return j_count
