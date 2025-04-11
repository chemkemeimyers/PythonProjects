class Solution(object):
    def solve(self,x:int)->int:
        steps = [1,2,3,4,5]
            
        if (x % max(steps) > 0):
            return x // max(steps) + 1
        else:
            return x // max(steps)


sol = Solution()
print(sol.solve(41))

