class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if '*' in p and '.' in p:
            if s != '':
                return True
            else:
                return False
        elif '*' in p:
            target = p[0]
            if target in s:
                return True
            else:
                return False
        elif '.' in p:
            if s != '':
                return True
            else:
                return False
        else:
            if s == p:
                return True
            else:
                return False
        