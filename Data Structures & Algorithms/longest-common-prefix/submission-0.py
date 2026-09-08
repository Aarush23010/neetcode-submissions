class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for j in range(len(strs[0])):
            var = strs[0][j]
            for i in range(len(strs)):
                if j>=len(strs[i]) or strs[i][j] != var:
                    return strs[0][:j]
        return strs[0]
    
            
