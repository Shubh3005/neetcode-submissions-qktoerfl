class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res+=str(len(i))+'#'+i
        print(res)
        return res
        # res= ''
        # for i in strs:
        #     res+=str(len(i))+"#"+ i
        # print(res)
        # return res
    def decode(self, s: str) -> List[str]:
        print(s)
        i=0
        res=[]
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            print(length)
            res.append(s[j+1:j+length+1])
            print(res)
            i=1+j+length
        return res

       
       
       
       
       
       
       
       
        # res =[]
        # i = 0
        # while i<len(s):
        #     j= i
        #     while s[j] != "#":
        #         j+=1
        #     length= (int(s[i:j]))
        #     res.append(s[j+1: j+1+length])
        #     i=j+1+length
        # return res