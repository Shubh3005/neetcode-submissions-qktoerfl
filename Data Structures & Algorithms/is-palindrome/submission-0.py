class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = self.cleanString(s)
        return res[::-1] == res

    def cleanString(self,s):
        res= []
        for i in s:
            if i.isalpha() or i.isnumeric():
                res.append(i.lower())
        return res