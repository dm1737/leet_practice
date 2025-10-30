from collections import defaultdict, List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        lose_count = defaultdict(int)
        
        for val in matches:
            winners.add(val[0])
            lose_count[val[1]] += 1
        
        undefeated = []
        for winner in winners:
            if winner not in lose_count:
                undefeated.append(winner)
        
        losers = list(lose_count.keys())
        for loser in lose_count:
            if lose_count[loser] > 1:
                losers.remove(loser)
            
        ans = []
        undefeated.sort()
        losers.sort()
        ans.append(undefeated)
        ans.append(losers)
        
        return ans
