class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        i=0
        while i< len(temperatures):
            print(temperatures[i])
            while stack and temperatures[i] > temperatures[stack[-1]]:
                    prev = stack.pop()
                    res[prev] = i - prev
            stack.append(i)
            i+=1
        return res
                