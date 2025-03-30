class Solution(object):
    def solve(self,n:int,m:int,a:int,b:int)->int:
        result = (n//m * b) + (n%m * a)

        result1 = (n//m + 1) * b

        result3 = n*a

        finalResult = min(result, result1, result3)

        return finalResult
    
sol = Solution()
print(sol.solve(10, 2, 1, 1))