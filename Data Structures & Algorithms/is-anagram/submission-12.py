class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        sHash={}
        tHash={}
        for i in range(len(s)):
            sHash[s[i]]= sHash.get(s[i],0)+1
            sHash[t[i]]= sHash.get(t[i],0)-1
        for i in sHash.values():
            if i !=0:
                return False
        return True