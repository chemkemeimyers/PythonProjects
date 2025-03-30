from typing import List
class Solution(object):
    def solve(self,l:List[int])->int:
    
        def countZeros(n):
                count = 0
                for i in n:
                    if i & 1 == 0:
                        count += 1
                return count
        
        print(len(l))
        for i in range (1,len(l)-1):
            print(i)
            print(countZeros(l[1:len(l)]))

            
    
    

    
sol = Solution()
sol.solve([1,0,1])
   