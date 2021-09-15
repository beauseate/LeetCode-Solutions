class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        low = 0
        high = len(height)-1
        currMax = 0
        while(low < high):
            currMax = max(currMax, min(height[low], height[high]) * (high - low))
            
            if(height[high] > height[low]):
                low += 1
            else:
                high -= 1
                
        return currMax
        