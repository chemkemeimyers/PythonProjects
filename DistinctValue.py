class Solution(object):
    def solve(self,a:int,b:int,c:int)->int:
        nums = [a,b,c]
        result= {}
        for i in nums:
            if i not in result.keys():
                result[i] = 1
            else:
                result[i] = result[i]+1
        
        for i in result.keys():
            if result[i] == 1:
                return i

sol = Solution()
print(sol.solve(1,2,2))