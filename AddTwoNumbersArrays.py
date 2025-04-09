class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        strVal1 = ""
        for i in l1:
            strVal1 += str(i)
        
        ReversedVal1 = strVal1[::-1]

        strVal2 = ""
        for j in l2:
            strVal2 += str(j)

        ReversedVal2 = strVal2[::-1]

        result = int(ReversedVal1)+int(ReversedVal2)

        strResult = str(result)

        reversedStrResult = strResult[::-1]

        arrayResult = []

        for char in reversedStrResult:
            arrayResult.append(int(char))
        
        return arrayResult
    
l1 = [2,4,3]
l2 = [5,6,4]

sol = Solution()

print(sol.addTwoNumbers(l1,l2))