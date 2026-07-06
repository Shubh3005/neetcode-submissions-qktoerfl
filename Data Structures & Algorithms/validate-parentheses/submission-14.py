class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif stack and i == ")" and stack[-1]=="(":
                stack.pop()
            elif stack and i == "}" and stack[-1]=="{":
                stack.pop()
            elif stack and i == "]" and stack[-1]=="[":
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True
        # stack = []
        # for i in s:
        #     if i in "({[":
        #         stack.append(i)
        #     elif stack and i == ")" and stack[-1]=="(":
        #         stack.pop()
        #     elif stack and i == "}" and stack[-1]=="{":
        #         stack.pop()
        #     elif stack and i == "]" and stack[-1]=="[":
        #         stack.pop()
        #     else:
        #         return False
        # if stack == []:
        #     return True
        # return False
