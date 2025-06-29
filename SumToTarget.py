def two_sum(nums, target):
    """
    Given a list of integers and a target number, return the indices of the two numbers that add up to the target

    Input: 
    nums: List of integers
    target: The value of which we need to identify indices in nums that tally to it 
    """

    for i in range(len(nums)):
        sublist = nums[i+1:len(nums)]
        for j in range(len(sublist)):
            if((nums[i] + sublist[j]) == target):
                secondIndex = i + 1 + j
                result = [i, secondIndex]
                return result

def efficient_two_sum(nums, target):
    """
    Given a list of integers and a target number, return the indices of the two numbers that add up to the target

    Input: 
    nums: List of integers
    target: The value of which we need to identify indices in nums that tally to it 
    """
    seen = {} # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return[seen[complement], i]
        seen[num] = i




print(two_sum([2, 7, 11, 15], 9))
print(efficient_two_sum([2, 7, 11, 15], 9))