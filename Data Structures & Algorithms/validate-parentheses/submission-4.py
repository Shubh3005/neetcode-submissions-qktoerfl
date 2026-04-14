class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for i in range(len(s)):
            print(s[i], stack)
            if s[i] in "([{":
                stack.append(s[i])
            elif s[i] == (")"):
                if not stack or stack.pop() != ("("):
                    return False
            elif s[i] == ("}"):
                if not stack or stack.pop() != ("{"):
                    return False
            elif s[i] == ("]"):
                if not stack or stack.pop() != ("["):
                    return False
        if stack:
            return False    
        return True