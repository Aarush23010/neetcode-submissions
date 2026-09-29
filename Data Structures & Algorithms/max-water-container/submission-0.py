class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        
        max_vol = 0
        while i<j:
            volume =  min(heights[i],heights[j])*(j-i)
            if volume > max_vol:
                max_vol = volume
            if heights[i]<heights[j]:
                i = i+1
            else:
                j = j-1
            
        return max_vol


            