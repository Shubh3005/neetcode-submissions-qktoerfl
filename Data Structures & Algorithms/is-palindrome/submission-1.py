class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer1= s[0]
        pointer2= s[-1]
        str1=[]
        s = s.lower()
        for i in s:
            if i.isalnum():
                str1.append(i)
        print(str1)
        return str1 == str1[-1::-1]
            