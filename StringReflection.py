class Solution(object):
    def solve(self, s:str) -> str:
        reversedString = ""
        for i in range (len(s)-1, -1, -1):
            reversedString = reversedString + s[i]    
            print(reversedString)

        ReflectionMatching = {"b":"d","d":"b","w":"w"}
        reflection = ""
        for i in reversedString:
            reflection+=ReflectionMatching[i]
        return reflection

sol = Solution()
print(sol.solve("dwd"))