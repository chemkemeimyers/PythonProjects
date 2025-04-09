from typing import List

class Solution(object):
    def solve(self,nums:List[List[int]]) -> List[int]:
        result = [0, 0, 0]
        for sublist in nums:
                result[0] += sublist[0]
                result[1] += sublist[1]
                result[2] += sublist[2]
        return [-x for x in result]

sol = Solution()
sol.solve(input)