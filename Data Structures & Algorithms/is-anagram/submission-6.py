from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        sHash = {}
        tHash = {}
        for i in range(len(s)):
            sHash[s[i]]= sHash.get(s[i],0)+1
            tHash[t[i]]= tHash.get(t[i],0)+1
        for i in sHash:
            if sHash[i]!= tHash.get(i,0):
                return False
        print(sHash)
        print(tHash)
        return True