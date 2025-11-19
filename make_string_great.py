class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        stack = []
        for c in s:
            if stack and stack[-1].lower() == c.lower():
                if stack[-1] == c:
                    stack.append(c)
                else:
                    stack.pop()
            else:
                stack.append(c)
                
        return "".join(stack)
