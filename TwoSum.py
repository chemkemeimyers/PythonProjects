class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            for j in nums[1:]:
                sum = i + j
                if (sum == target):
                    if(i==j):
                        return [nums.index(i), nums.index(j, nums.index(i)+1)]
                    else:
                        return [nums.index(i), nums.index(j)]
                
sol = Solution()
print(sol.twoSum([3,2,4], 6))